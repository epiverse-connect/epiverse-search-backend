import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential


def get_blob_service_client():
    env = os.getenv("env")
    conn_str = os.getenv("AzureWebJobsStorage")
    if env == "local" and conn_str:
        return BlobServiceClient.from_connection_string(conn_str)
    else:
        account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
        if not account_name:
            raise ValueError("AZURE_STORAGE_ACCOUNT_NAME environment variable must be set when using DefaultAzureCredential.")
        account_url = f"https://{account_name}.blob.core.windows.net"
        credential = DefaultAzureCredential()
        return BlobServiceClient(account_url=account_url, credential=credential)