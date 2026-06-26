# Flask MongoDB Kubernetes 

## Overview

This project demonstrates the deployment of a Flask application integrated with MongoDB on Kubernetes using Minikube and Docker.

The application exposes REST APIs, connects to MongoDB, and returns a JSON response containing the assignment message along with the current date and time.

---

## Technologies Used

- Python 3.11
- Flask
- MongoDB
- Docker
- Kubernetes
- Minikube

---

## Project Structure

```
flask-mongodb-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
│
├── k8s/
│   ├── flask-development.yaml
│   ├── flask-service.yaml
│   ├── mongodb-statefulset.yaml
│   ├── mongodb-service.yaml
│   ├── pv.yaml
│   ├── pvc.yaml
│   ├── hpa.yaml
│   ├── secret.yaml
│   └── screenshots/
│       ├── output.png
│       ├── python-app.png
│       ├── pods.png
│       └── docker.png
```

---

## Features

- Flask REST API
- MongoDB Integration
- Dockerized Application
- Kubernetes Deployment
- Persistent Volume Configuration
- Horizontal Pod Autoscaler (HPA)
- Returns JSON response with:
  - Assignment Message
  - Current Date
  - Current Time

---

## Docker Build

```bash
docker build -t flask-mongodb-app:latest .
```

---

## Run Docker Container

```bash
docker run --rm flask-mongodb-app:latest
```

---

## Kubernetes Deployment

Apply all Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Check Pods

```bash
kubectl get pods
```

Check Services

```bash
kubectl get services
```

Open Application

```bash
minikube service flask-service
```

---

## Expected Output

```json
{
  "message": "FarAlpha Kubernetes Assignment Running Successfully",
  "date": "DD-MM-YYYY",
  "time": "HH:MM:SS"
}
```

---

# Screenshots

# Screenshots

## 1. Flask Application Output

![Application Output](k8s/screenshots/Screenshot%202026-06-26%20100156.png)

---

## 2. Running Flask Application

![Python App](k8s/screenshots/Screenshot%202026-06-26%20100513.png)

---

## 3. Kubernetes Pods

![Pods](k8s/screenshots/Screenshot%202026-06-26%20100645.png)

---

## 4. Docker Container

![Docker](k8s/screenshots/Screenshot%202026-06-26%20100803.png)

## Author

**Nitish Kumar**
---

## GitHub Repository

https://github.com/Nitz981/flask-mongodb-app
