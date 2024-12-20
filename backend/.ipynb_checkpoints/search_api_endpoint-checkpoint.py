from fastapi import FastAPI, HTTPException, Query
from typing import List
from elasticsearch import Elasticsearch
from pydantic import BaseModel
#import numpy as np
from transformers import AutoTokenizer, AutoModel, pipeline
from elasticsearch import Elasticsearch
import torch
from fastapi.middleware.cors import CORSMiddleware




# Load the BERT tokenizer and model

# Initialize Elasticsearch client
# es = Elasticsearch("http://127.0.0.1:9200")
es = Elasticsearch("http://host.docker.internal:9200")


if es.ping():
    print("Successfully connected to Elasticsearch")
else:
    print("Elasticsearch connection failed")
    
    
# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('distilbert/distilbert-base-uncased')
# Initialize the FastAPI application
app = FastAPI(debug=True)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



model = AutoModel.from_pretrained('distilbert/distilbert-base-uncased')

# Define the request body structure using Pydantic
class UserQuery(BaseModel):
    query_user: str
    
# Define a route for the API
@app.get("/api/")
# def get_data(input:UserQuery):
#     # Python logic or function call here

#     query = input.query_user


def get_data(query:str = Query(..., description="User query string")):
    # Python logic or function call here
    print("Running search for this keyword -->:{}".format(query))
    inputs = tokenizer(query, return_tensors='pt', padding=True, truncation=True)
    
    with torch.no_grad():
        output = model(**inputs).last_hidden_state.mean(dim=1).squeeze(0).numpy()
        query_vector = output
        # Define the Elasticsearch kNN search
        search = {
            "knn": {
                "field": "embedding",
                "query_vector": query_vector.tolist(),
                "k": 5,
                "num_candidates": 100
                },
            "fields":[ "text" ]
            }
        # Perform the kNN search and print the results
        response = es.search(index='embedding_v2', body=search)
        print(response)
    case_list = []
    
    #print(response)
    for hit in response['hits']['hits']:
        print(hit['_source'])
        case = {
                'Package Name': hit['_source']['package_name'], 
                'File Name' : hit['_source']['file_name'],
                'Score': hit['_score']
        }
        case_list.append(case)

    # Return the data as a JSON response
    return case_list

