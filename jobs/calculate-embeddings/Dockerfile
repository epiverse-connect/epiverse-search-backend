# -----------------------------------------------------------------
# jobs/calculate‐embeddings/Dockerfile
# -----------------------------------------------------------------

# 1) Start from a slim Python base
FROM python:3.10-slim

# 2) Install system libraries for R, Torch, etc.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        gnupg \
        curl \
        git \
        # R runtime and dev libs:
        r-base \
        libcurl4-openssl-dev \
        libssl-dev \
        # ICU for text processing (often needed by sentence-transformers):
        libicu-dev \
        # Build tools for some Python packages if needed
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3) Install renv and restore R packages (per your renv.lock)
COPY renv.lock .
RUN Rscript -e "install.packages('renv', repos='https://cloud.r-project.org')" && \
    Rscript -e "renv::restore()"

# 4) Set working directory
WORKDIR /app

# 5) Copy Python requirements and install them
COPY requirements.txt .
# Add dependencies for sentence-transformers, torch, huggingface, etc., if not in requirements.txt:
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt_tab

# 6) Copy in your helper modules, logging config, and the main runner
# COPY logging_config.yaml .
# optional: keep your helper separate, if you want
COPY utils.py ./utils.py
COPY calculate_embeddings.py ./calculate_embeddings.py   
COPY run_calculate_embeddings.py ./run_calculate_embeddings.py

# 7) Environment variables
ENV env=production
ENV AZURE_STORAGE_ACCOUNT_NAME=

# 7) Ensure run_calculate_embeddings is executable (not strictly needed, but good practice)
RUN chmod +x ./run_calculate_embeddings.py

# 8) Default command: run the embedding pipeline
ENTRYPOINT ["python", "run_calculate_embeddings.py"]
