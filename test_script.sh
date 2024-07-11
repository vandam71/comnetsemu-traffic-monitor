#!/bin/bash

# Start Docker services with Docker Compose
echo "Starting Docker services..."
docker-compose up -d
echo "Docker services started."


# Run Ryu controller (Traffic Monitor)
echo "Starting Ryu controller..."
ryu-manager traffic_monitor_v1.py &


# Run Python topology script
echo "Running Python topology script..."
sudo python3 topology.py

echo "Script execution completed."
