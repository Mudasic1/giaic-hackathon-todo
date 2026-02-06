Phase IV Spec: Local Kubernetes Deployment

1. Overview

The goal of Phase IV is to evolve the Todo Chatbot from a standalone full-stack application into a containerized, orchestrated system running locally on a Kubernetes cluster. This phase introduces Cloud-Native principles, infrastructure as code (Helm), and AIOps workflows.

2. Technology Stack

Component

Technology

Containerization

Docker (Docker Desktop)

Docker AI Assistant

Docker AI Agent (Gordon)

Orchestration

Kubernetes (Minikube)

Package Management

Helm Charts

AIOps Tools

kubectl-ai, kagent

Base Application

Phase III Todo Chatbot (FastAPI + Next.js + Agents SDK)

3. Requirements

3.1 Containerization

Frontend Container: Dockerize the Next.js application using an optimized multi-stage build.

Backend Container: Dockerize the FastAPI application (including the MCP server logic).

Docker AI (Gordon): Use Gordon to assist in generating optimized Dockerfiles and troubleshooting container builds.

3.2 Kubernetes Orchestration

Cluster: Use minikube as the local Kubernetes environment.

Helm Charts:

Create a unified Helm chart (or separate sub-charts) for the Todo App.

Define values.yaml for environment-specific configurations (Database URLs, API Keys).

Implement Readiness and Liveness probes for both services.

Networking:

Use Kubernetes Services (ClusterIP/NodePort) for internal communication.

Use Ingress or minikube tunnel to expose the frontend.

3.3 AIOps Integration

kubectl-ai: Use natural language to generate manifests and perform cluster operations (e.g., "deploy the todo frontend with 2 replicas").

kagent: Use for cluster health analysis and resource optimization.

4. Architecture Diagram (Local K8s)

[ User Browser ] 
      │
      ▼
[ Minikube Cluster ]
      │
      ├─► [ Ingress / Service ]
      │         │
      │         ├─► [ Frontend Pods (Next.js) ]
      │         │
      │         └─► [ Backend Pods (FastAPI + MCP) ]
      │                   │
      └─► [ External Neon DB (PostgreSQL) ]


5. Deployment Workflow (Spec-Driven)

Specify: Update speckit.specify to include Kubernetes resources (Deployments, Services, ConfigMaps).

Plan: Define the infrastructure layout in speckit.plan.

Tasks: Break down into atomic tasks:

T401: Write Dockerfiles for Frontend and Backend.

T402: Initialize Helm chart structure.

T403: Configure Kubernetes Secrets for Database and OpenAI keys.

T404: Deploy to Minikube using helm install.

Implement: Use Claude Code to execute tasks. No manual manifest writing allowed.

6. Acceptance Criteria

[ ] Both Frontend and Backend images are successfully pushed to a local or public registry.

[ ] helm install successfully deploys all components without manual kubectl intervention.

[ ] Pods scale correctly when using kubectl-ai commands.

[ ] The Chatbot is accessible via a local browser URL and maintains state via the Neon DB.

[ ] Resource limits and requests are defined to prevent cluster exhaustion.

7. Commands Reference

# Start Minikube
minikube start

# Generate manifests via AI
kubectl-ai "create a deployment for the backend using image todo-backend:latest"

# Deploy via Helm
helm upgrade --install todo-app ./charts/todo-app -f values.yaml

# Analyze Health
kagent "check why the backend pods are in ImagePullBackOff"
