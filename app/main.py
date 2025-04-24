from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from models import UserQuery, SearchResponse
from search_engine import SemanticSearchEngine
from utils import setup_logging
import json
import logging
import json
import os


# Setup logging
setup_logging()
logger = logging.getLogger('main')


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

# Initialize the search engine when the app starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

search_engine = SemanticSearchEngine(
    corpus_embeddings_path=os.path.join(DATA_DIR, "corpus_embeddings.pth"),
    analysis_df_path=os.path.join(DATA_DIR, "analysis_df.csv"),
    package_descr_path=os.path.join(DATA_DIR, "epipkgs_metadata.json"),
    device="cpu"  # Or "cuda" if available
)

@app.get("/api/", response_model=SearchResponse)
def get_data(query: str = Query(..., description="User query string")):
    logger.info("Input question:{query}") 
    results = search_engine.search(query)
    json_response = {
        "query": query,
        "filter": "epiverse",
        "response": {
            "results": results,
        }
    }
    logger.info("Response:{json_response}") 
    return json_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)