import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time
import requests
from elasticsearch import helpers
import csv
import io
import ast
# Wait for Elasticsearch to start
#time.sleep(20)

# Connect to Elasticsearch
#es = Elasticsearch("http://host.docker.internal:9200")
#es = Elasticsearch("http://192.168.16.2:9200")
es = Elasticsearch("http://0.0.0.0:9200", timeout=900)
#es = Elasticsearch("http://elasticsearch_demo_gambia:9200", timeout=900)

if es.ping():
    print("Successfully connected to Elasticsearch")
else:
    print("Elasticsearch connection failed")

# URL of the CSV file
csv_url = "https://epiverse-search-embeddings-public.s3.us-east-1.amazonaws.com/embedding_df_with_vignette.csv"

# Download the CSV file
print("Getting the CSV file from S3.")
response = requests.get(csv_url)

if response.status_code == 200:
    with open("data.csv", "wb") as file:
        file.write(response.content)
else:
    print(f"Failed to download CSV. Status code: {response.status_code}")
    exit(1)

# Read the CSV file
df = pd.read_csv("data.csv")


#try:
#    es.indices.delete(index="embedding_v2")
#    print("Deleted older embedding index")
#except:
#    print("unable to delete older index")


mapping = {
    "properties": 
        {

    "package_name": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 768
          }
        }
      },
           
     "file_name": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "content": {
        "type": "text",
        "analyzer": "standard"
      },
    "embedding": {
        "type": "dense_vector",
        "dims": 768,
        "index": 'true',
            "similarity": "cosine",
          },

        } 
  }    
# Create an index with the defined mapping

#es.indices.create(index='embedding_v2', body={'mappings': mapping}, ignore =400)



#es.options(request_timeout=90).indices.create(index='embedding_v2', body={'mappings': mapping}, ignore =400)



#time.sleep(20)

INDEX_NAME = "embedding_v2"
def get_csv_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch CSV from URL. Error: {e}")

# Function to add data row by row to Elasticsearch
def add_row_to_elasticsearch(es_client, index_name, row):
	try:
        # Insert row into Elasticsearch
#        response = es_client.index(index=index_name, document=row)
		response = es_client.options(request_timeout=30).index(index=index_name, document=row)
		print(f"Inserted document with ID: {response['_id']}")
	except Exception as e:
        # Raise an error if there's an issue
		raise Exception(f"Failed to insert row: {row}. Error: {e}")

# Process CSV and upload rows to Elasticsearch
def process_csv_and_upload_to_elasticsearch(csv_content, es_client, index_name):
	csv_reader = csv.DictReader(io.StringIO(csv_content))
	for row in csv_reader:
		row['embedding']= parse_vector(row['embedding'])
		add_row_to_elasticsearch(es_client, index_name, row)


# Function to parse and sanitize vectors
def parse_vector(vector_str):
    try:
        # Safely convert string representation of list into an actual list
        vector = ast.literal_eval(vector_str)
        if isinstance(vector, list):
            return [float(x) for x in vector]  # Ensure all elements are floats
        else:
            raise ValueError("Parsed vector is not a list.")
    except Exception as e:
        raise ValueError(f"Failed to parse vector: {vector_str}. Error: {e}")
   
        
csv_content = get_csv_from_url(csv_url)

    
# Process and upload data to Elasticsearch
try:
	process_csv_and_upload_to_elasticsearch(csv_content, es, INDEX_NAME)
	print(f"All rows from the S3 file were successfully uploaded.")
except Exception as e:
	print(f"Error during upload:{e}")

print("Data loaded successfully.")
