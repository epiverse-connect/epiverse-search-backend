FROM python:3.11-slim

WORKDIR /app

COPY load_data.py .
COPY /backend/requirements.txt .
COPY /backend/search_api_endpoint.py .

RUN pip install pandas elasticsearch requests
RUN pip install -r requirements.txt
#EXPOSE 8000

# 
# RUN pip install -r requirements.txt

CMD ["python3", "load_data.py"]
