FROM pytorch/torchserve

WORKDIR /jobs
COPY calculate_embedding.py .
COPY requirements.txt .
COPY logging_config.yaml .
COPY sources /sources/

RUN pip install -r requirements.txt
RUN pip install azure-functions azure-storage-blob azure-identity

CMD ["python3", "calculate_embedding.py"]




FROM mcr.microsoft.com/azure-functions/python:4-python3.10

# Copy function app files
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY . /home/site/wwwroot




