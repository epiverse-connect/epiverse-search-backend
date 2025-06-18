import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
import logging


def get_blob_service_client():
    env = os.getenv("env")
    conn_str = os.getenv("AzureWebJobsStorage")
    # If running locally, use the connection string from environment variable
    logging.info(f"env: {env}", f"conn_str: {conn_str}")
    if env == "local" and conn_str:
        logging.info("Using local Azure Blob Storage connection string.")
        return BlobServiceClient.from_connection_string(conn_str)

    # If running in Azure, use DefaultAzureCredential
    else:
        logging.info("Using Azure Blob Storage with DefaultAzureCredential.")
        account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
        if not account_name:
            raise ValueError("AZURE_STORAGE_ACCOUNT_NAME environment variable must be set when using DefaultAzureCredential.")
        account_url = f"https://{account_name}.blob.core.windows.net"
        credential = DefaultAzureCredential()
        return BlobServiceClient(account_url=account_url, credential=credential)