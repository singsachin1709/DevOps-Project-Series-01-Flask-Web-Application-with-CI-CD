#!/bin/bash
echo "🔍 Running Tests..."
if ! pytest tests/; then
    echo "❌ Tests Failed. Exiting build."
    exit 1
fi

echo "🐳 Building Docker Image..."
docker build -t sachin-devops-dashboard .

echo "🛑 Removing Existing Container..."
docker rm -f sachin-devops-dashboard || true

echo "🚀 Running New Container..."
docker run -d --name sachin-devops-dashboard -p 5000:5000 sachin-devops-dashboard
