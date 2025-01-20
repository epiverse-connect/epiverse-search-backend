FROM python:3.11-slim

WORKDIR /app

COPY pkg_metadata_api.csv .
#COPY corpus_embeddings.pth .
#COPY /backend/requirements.txt .
#COPY /backend/search_api_endpoint.py .
COPY ./app/ .

RUN pip install pandas requests
RUN pip install -r requirements.txt
EXPOSE 8000

# 
# RUN pip install -r requirements.txt

#CMD ["python3", "load_data.py"]
CMD ["echo" ,"Success!"]
