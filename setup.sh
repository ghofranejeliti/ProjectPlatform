#!/bin/bash

echo "🚀 Starting Mini Platform Setup..."

# Step 1: Build Docker image
echo " Building Docker image..."
docker build -t platform .

# Step 2: Stop old container if running
echo " Stopping old container (if exists)..."
docker stop platform 2>/dev/null
docker rm platform  2>/dev/null

# Step 3: Run new container
echo "  Starting container..."
docker run -d -p 5000:5000 --name platform platform 

# Step 4: Wait for app to start
echo " Waiting for app to start..."
sleep 3

# Step 5: Test the endpoints
echo " Testing /health endpoint..."
curl http://localhost:5000/health

echo -e "\n\n Testing /data endpoint..."
curl http://localhost:5000/data

echo -e "\n\n Setup complete!"
echo " Visit http://localhost:5000/status to see the dashboard"
echo " To stop: docker stop platform "