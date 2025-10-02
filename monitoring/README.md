<h1> Problem Statement 1 — Wisecow: Containerization & Kubernetes Deployment
📌 Overview</h1>

The Wisecow project demonstrates the complete DevOps pipeline:

  Containerization with Docker

  Deployment to Kubernetes

  CI/CD automation with GitHub Actions

  Secure communication with TLS & Ingress

This transforms a simple Bash-based app into a production-ready, secure service.

<h3>⚙️ Steps Implemented </h3>
  Dockerization (Dockerfile)

  Created a Dockerfile to package the Wisecow app.

  Built and tested locally using:

    docker build -t wisecow-app .
    docker run -p 4499:4499 wisecow-app


<h3>Verified by visiting:</h3>

    http://localhost:4499

Kubernetes Deployment (k8s/deployment.yaml & k8s/service.yaml)

<h3>Created a Deployment to run Wisecow as Pods.</h3>

    Exposed it as a Service for cluster access.

<h3>Verified using:</h3>

    kubectl get pods
    kubectl get svc
    kubectl port-forward svc/wisecow-service 4499:80


<h3>Checked in browser:</h3>

    http://localhost:4499 

<h3>CI/CD Pipeline (.github/workflows/ci-cd.yaml)</h3>

    Implemented GitHub Actions workflow:

    On push to main:

Builds Docker image

Pushes to Docker Hub → abhitete/wisecow:latest

TLS + Ingress (k8s/ingress.yaml)

Installed NGINX ingress controller.

Generated self-signed TLS certificate:

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -out tls.crt -keyout tls.key \
  -subj "/CN=wisecow.local/O=wisecow"
kubectl create secret tls wisecow-tls --cert=tls.crt --key=tls.key


Configured Ingress for HTTPS.

Updated hosts file:

127.0.0.1 wisecow.local


Verified secure access at:

https://wisecow.local
----
📂 Project Structure
wisecow-k8s/
│── wisecow.sh             
│── Dockerfile             
│── k8s/
│    ├── deployment.yaml    
│    ├── service.yaml       
│    └── ingress.yaml       
│── .github/
│    └── workflows/
│         └── ci-cd.yaml    
│── tls.crt                 
│── tls.key                 
│── README.md               

🎯 End Goal Achieved

✅ Containerized Wisecow app

✅ Deployed to Kubernetes

✅ Automated CI/CD pipeline

✅ Secured with TLS & Ingress

<h2>🖥️ Problem Statement 2 — Monitoring & Health Checks
📌 Overview</h2>

This project implements two automation scripts using Python:

System Health Monitoring Script

Monitors CPU, memory, disk usage, and top running processes.

Logs alerts if thresholds are exceeded.

Application Health Checker

Checks if a web application (like Wisecow) is UP or DOWN.

Uses HTTP status codes to determine availability.

<h3>⚙️ Scripts</h3>h3>
System Health Monitoring (system_health.py)

Checks:

CPU usage (> 80%)

Memory usage (> 80%)

Disk usage (> 80%)

Logs top 5 processes by memory usage.

Results saved in system_health.log.

Run:

py system_health.py


Check logs:

type system_health.log

Application Health Checker (app_health.py)

Sends an HTTP request to a given URL.

If status code = 200 → App is UP

Else → App is DOWN

Results saved in app_health.log.

Run:

py app_health.py


Check logs:

type app_health.log

📂 Project Structure
monitoring/
│── system_health.py    
│── app_health.py       
│── system_health.log   
│── app_health.log      
│── README.md           

🛠️ Requirements

Python 3.8+

Install dependencies:

py -m pip install psutil requests

<h2>🎯 End Goal Achieved

✅ Automated system monitoring with alerts

✅ Application health checker via HTTP

✅ Logs saved for auditing</h2>
