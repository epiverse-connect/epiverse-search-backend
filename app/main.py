from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from models import UserQuery, SearchResponse
from search_engine import SemanticSearchEngine
import json
import logging.config
from logging.handlers import RotatingFileHandler
import yaml


# --- Logging Configuration ---
with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


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
search_engine = SemanticSearchEngine(
    corpus_embeddings_path="../data/corpus_embeddings.pth",
    analysis_df_path="../data/analysis_df.csv",
    package_descr_path="../data/epipkgs_metadata.json",
    device="cpu" # Or "cuda" if available
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