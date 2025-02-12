from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel
#import numpy as np
from transformers import AutoTokenizer, AutoModel, pipeline
import torch
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import pickle
import json
import pandas as pd 
device = torch.device("cpu")



## Custome functions 
def get_value(df, column, condition):
    try:
        return df.loc[condition, column].iloc[0]
    except IndexError:
        return None


## Data processing steps

print("Loading embeddings from 'embeddings.pkl'...")
corpus_embeddings = torch.load("corpus_embeddings.pth",map_location=torch.device('cpu'))

print("Loaded emeddings.")
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
bi_encoder.max_seq_length = 256    #Truncate long passages to 256 tokens
top_k = 32                          #Number of passages we want to retrieve with the bi-encoder

#The bi-encoder will retrieve 32 documents. We use a cross-encoder, to re-rank the results list to improve the quality
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

analysis_df_prev = pd.read_csv('analysis_df.csv')
#package_descr_df = pd.read_csv('pkg_metadata_api.csv')
package_descr_df = pd.read_json("epipkgs_metadata.json",dtype =str)
package_descr_df.columns = ['package','logo','website', 'source', 'articles']
package_descr_df = package_descr_df.map(lambda x: str(x)[2:-2])


analysis_df = analysis_df_prev.merge(package_descr_df, left_on='package_name', right_on='package', how='left')


app = FastAPI(debug=True)

origins = [
	"http://localhost",
	"http://localhost:8080",
	"http://localhost:8000",
	"epiverse-connect.github.io"
	]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
	)

paragraphs = [str(s) for s in analysis_df['tokenized_content'].to_list()]
# Smaller value: Context from other sentences might get lost
# Lager values: More context from the paragraph remains, but results are longer
window_size = 7
passages= []

for start_idx in range(0, len(paragraphs), window_size):
    end_idx = min(start_idx + window_size, len(paragraphs))
    passages.append(";".join(paragraphs[start_idx:end_idx]))


# Define the request body structure using Pydantic
class UserQuery(BaseModel):
	query_user: str
    
# Define a route for the API
@app.get("/api/")
# def get_data(input:UserQuery):
#     # Python logic or function call here

#     query = input.query_user

def get_data(query:str = Query(..., description="User query string")):
	print("Input question:", query)

    ##### Semantic Search #####
    # Encode the query using the bi-encoder and find potentially relevant passages
	question_embedding = bi_encoder.encode(query, convert_to_tensor=True)
	question_embedding = question_embedding.to(device)
	hits = util.semantic_search(question_embedding, corpus_embeddings, top_k=top_k)
	hits = hits[0]  # Get the hits for the first query

    ##### Re-Ranking #####
    # Now, score all retrieved passages with the cross_encoder
	cross_inp = [[query, passages[hit['corpus_id']]] for hit in hits]
	cross_scores = cross_encoder.predict(cross_inp)

    # Sort results by the cross-encoder scores
	for idx in range(len(cross_scores)):
		hits[idx]['cross-score'] = cross_scores[idx]


	temp_df_CER_list = []
    # Output of top-5 hits from re-ranker
	hits = sorted(hits, key=lambda x: x['cross-score'], reverse=True)
	for hit in hits[0:20]:
		package_name = get_value(analysis_df, 'package_name', analysis_df['cluster_id'] == hit['corpus_id'])
		logo= get_value(analysis_df, 'logo', analysis_df['cluster_id']==hit['corpus_id'])
		website = get_value(analysis_df, 'website', analysis_df['cluster_id']==hit['corpus_id'])
		source_package= get_value(analysis_df, 'source', analysis_df['cluster_id']==hit['corpus_id'])
		vignettes=["To be added to scrapper"]
		temp_df_CER_list.append([package_name,logo,website,source_package,vignettes ,str(round(hit['score'],4))])

	temp_df_CER = pd.DataFrame(temp_df_CER_list)
	temp_df_CER = temp_df_CER.drop_duplicates([0], keep='first')
	temp_df_CER.columns =["package_name","logo","website","source","vignettes","relevance"]
	temp_df_CER = temp_df_CER.sort_values(by='relevance', ascending=False)	

	results = [row.to_dict() for _, row in temp_df_CER.head(5).iterrows()]

	json_response = {
		"query": query,
		"filter": "epiverse",
		"response" : {
			"results": results,
		}
	}
	json_string = json.dumps(json_response, allow_nan=True)
	return Response(content=json_string, media_type="application/json")
