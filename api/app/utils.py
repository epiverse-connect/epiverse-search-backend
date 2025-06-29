import pandas as pd
import logging.config
import yaml
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import AzureError
import tempfile

def setup_logging(default_path='logging_config.yaml', default_level=logging.INFO):
    """Setup logging configuration"""
    try:
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', default_path)
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                # Ensure logs directory exists
                os.makedirs('logs', exist_ok=True)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            logging.warning(f"Logging config file not found at {config_path}")
    except Exception as e:
        logging.basicConfig(level=default_level)
        logging.error(f"Error in logging setup: {str(e)}")

        
def get_value(df: pd.DataFrame, column: str, condition: pd.Series):
    try:
        return df.loc[condition, column].iloc[0]
    except IndexError:
        return None
    
def get_blob_service_client():
    # Check for required environment variables for shared key
    env = os.getenv("env")

    if env == "local":
        # Use Shared Key credential
        connection_str=os.getenv("AzureWebJobsStorage")
        if not connection_str:
            logging.error("AzureWebJobsStorage environment variable is not set or empty!")
            raise ValueError("AzureWebJobsStorage is required but not provided.")
        return BlobServiceClient.from_connection_string(connection_str)

    else:
        # Use DefaultAzureCredential

        account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")

        if account_name:
            account_url = f"https://{account_name}.blob.core.windows.net"

        else:
            raise ValueError("AZURE_STORAGE_ACCOUNT_NAME is required.")

        logging.info("Trying DefaultAzureCredential")
        try: 
            credential = DefaultAzureCredential()
            return BlobServiceClient(account_url=account_url, account_name=account_name, credential=credential)

        except AzureError as e:
            logging.error(f"Failed to authenticate with DefaultAzureCredential: {e}")
            raise


def load_data_from_blob(container_name: str, blob_name: str, file_type: str):
    """
    Load embeddings from Azure Blob Storage.
    
    Returns:
        torch.Tensor: The loaded embeddings.
    """
    
    blob_service_client = get_blob_service_client()
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Temporary file path
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name

    try:
        # Download the blob in chunks and write to the temp file
        with open(temp_file_path, "wb") as file:
            logging.info(f"Downloading {blob_name} to {temp_file_path}")
            download_stream = blob_client.download_blob()
            for chunk in download_stream.chunks():
                file.write(chunk)
        logging.info(f"Downloaded {blob_name} to {temp_file_path}")
        return temp_file_path
    except  Exception as e:
        logging.error(f"Unable to load file {blob_name}: {e}")
        