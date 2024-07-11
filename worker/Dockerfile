# Use Python 3.9 Alpine as base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run your application
CMD ["python", "worker.py"]