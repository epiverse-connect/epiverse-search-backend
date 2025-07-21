import sys
import json
import logging
from fetch_universe_metadata import fetch_universe_metadata
from utils import get_blob_service_client

# — Configure logging to stdout (Container Apps captures stdout automatically) —
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s — %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def main():
    try:
        blob_service_client = get_blob_service_client()
    except Exception as e:
        logging.error(f"Failed to create BlobServiceClient: {e}", exc_info=True)
        sys.exit(1)

    container_name = "data"
    blob_name = "epipkgs_metadata.json"

    # Ensure the container exists
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
        logging.info(f"Created container '{container_name}'")
    except Exception:
        logging.info(f"Container '{container_name}' already exists (or creation failed).")


    # Fetch the metadata
    try:
        processed_metadata = fetch_universe_metadata("epiverse-connect")
        logging.info(f"Fetched metadata: {len(processed_metadata)} packages")
    except Exception as e:
        logging.error(f"Failed to fetch metadata: {e}", exc_info=True)
        sys.exit(1)

    # Upload the JSON to blob
    try:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(
            json.dumps(processed_metadata).encode("utf-8"),
            overwrite=True
        )
        logging.info(f"Uploaded metadata to blob '{container_name}/{blob_name}'")
    except Exception as e:
        logging.error(f"Failed to upload blob: {e}", exc_info=True)
        sys.exit(1)

    logging.info("Job completed successfully")
    sys.exit(0)


if __name__ == "__main__":
    main()