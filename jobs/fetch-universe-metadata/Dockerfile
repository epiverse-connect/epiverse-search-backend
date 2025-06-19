# 1. Start from a slim Python image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy in your helper module (fetch_universe_metadata) and script
COPY fetch_universe_metadata.py ./fetch_universe_metadata.py
COPY run_fetch_universe_metadata.py ./run_fetch_universe_metadata.py

# 5. Make the script executable
RUN chmod +x ./run_fetch_universe_metadata.py

# 6. Default command just runs the script
ENTRYPOINT ["python", "run_fetch_universe_metadata.py"]
