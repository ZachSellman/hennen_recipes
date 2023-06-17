
FROM python:3.11-slim AS builder

# This is neccesary step for psycopg2 to function in slim image
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Create virtual environment
RUN python -m venv /opt/venv
# Activate venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


# Operational stage
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Get venv from bulider stage
COPY --from=builder /opt/venv /opt/venv

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1\
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY . /app/