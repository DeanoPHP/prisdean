# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Prevent Python from writing .pyc files & enable stdout logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project (will be overridden by bind mount in dev)
COPY . /app/

# Command to run Django server
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
