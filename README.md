<h1>🐮 Wisecow — Kubernetes Deployment with CI/CD & TLS</h1>

<h2>📌 Project Overview</h2>

This project demonstrates the **containerization, deployment, CI/CD automation, and TLS security** of the Wisecow application.

We took a simple Bash-based app and:

- 🐳 Containerized it with Docker  
- ☸️ Deployed it to Kubernetes  
- 🔄 Automated build & push with GitHub Actions  
- 🔒 Secured it with TLS via Kubernetes Ingress  

---

<h2>🚀 Features Implemented</h2>

<h3>1. Dockerization</h3>

- Created a `Dockerfile` to package Wisecow app.  
- Tested with:  
  ```bash
  docker run -p 4499:4499 wisecow-app
<h3>2. Kubernetes Deployment</h3>
deployment.yaml → Runs the Wisecow app as Pods.

service.yaml → Exposes it inside the cluster.

Verified via kubectl port-forward and browser access.

<h3>3. CI/CD Pipeline (GitHub Actions)</h3>
On every push to main:

Builds the Docker image.

Pushes to Docker Hub → abhitete/wisecow:latest.

<h3>4. TLS + Ingress</h3>
Installed ingress-nginx controller.

Generated a self-signed TLS cert.

Created a Kubernetes TLS secret.

Configured ingress.yaml for HTTPS at → https://wisecow.local.

<h2>🛠️ Setup Instructions</h2> <h3>1. Clone Repository</h3>
bash
Copy code
git clone https://github.com/abhitete/wisecow-k8s.git
cd wisecow-k8s
<h3>2. Docker (Optional Local Run)</h3>
bash
Copy code
docker build -t wisecow-app .
docker run -p 4499:4499 wisecow-app
👉 Open → http://localhost:4499

<h3>3. Kubernetes Deployment</h3>
bash
Copy code
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
Check pods & service:

bash
Copy code
kubectl get pods
kubectl get svc
Access locally:

bash
Copy code
kubectl port-forward svc/wisecow-service 4499:80
👉 Then open → http://localhost:4499

<h3>4. TLS + Ingress</h3>
Generate TLS cert (self-signed):

bash
Copy code
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -out tls.crt -keyout tls.key \
  -subj "/CN=wisecow.local/O=wisecow"

kubectl create secret tls wisecow-tls --cert=tls.crt --key=tls.key
Apply Ingress:

bash
Copy code
kubectl apply -f k8s/ingress.yaml
Update hosts file (C:\Windows\System32\drivers\etc\hosts):

lua
Copy code
127.0.0.1 wisecow.local
👉 Access app securely → https://wisecow.local

<h3>5. CI/CD (GitHub Actions)</h3>
Workflow → .github/workflows/ci-cd.yaml

Runs on every push to main.

Builds and pushes Docker image → Docker Hub.

(Optional) Can be extended to deploy automatically to Kubernetes.

<h2>📂 Repository Structure</h2>
bash
Copy code

```
wisecow-k8s/
│── wisecow.sh              # Original application script
│── Dockerfile              # Docker image definition
│── k8s/
│    ├── deployment.yaml    # K8s Deployment
│    ├── service.yaml       # K8s Service
│    └── ingress.yaml       # K8s Ingress + TLS
│── .github/
│    └── workflows/
│         └── ci-cd.yaml    # GitHub Actions pipeline
│── README.md               # Documentation (this file)
```


<h2>🎯 End Goal Achieved</h2>
✅ Containerized Wisecow app
✅ Deployed on Kubernetes
✅ Automated CI/CD pipeline
✅ Secured with TLS over HTTPS


yaml
Copy code
