#!/bin/bash
set -e

echo "🚀 Deploying Wisecow application to local Kubernetes..."

# Make sure Kubernetes is running
kubectl cluster-info > /dev/null 2>&1 || {
    echo "❌ Kubernetes cluster not reachable. Start Docker Desktop or Minikube first."
    exit 1
}

# Apply manifests (deployment + service)
echo "📦 Applying Kubernetes manifests..."
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Update deployment to use latest image from Docker Hub
echo "🔄 Updating deployment with latest image..."
kubectl set image deployment/wisecow wisecow=abhitete/wisecow:latest --record

# Wait for rollout to finish
echo "⏳ Waiting for rollout to complete..."
kubectl rollout status deployment/wisecow

echo "✅ Deployment complete! Wisecow should be available on your service port."
