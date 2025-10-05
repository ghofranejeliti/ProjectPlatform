# Start with a base Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (Docker caching optimization)
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Create logs directory
RUN mkdir -p ../logs

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run when container starts
CMD ["python", "main.py"]