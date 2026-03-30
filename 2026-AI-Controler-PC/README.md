AI PLATFORM CONTROLLER
Great Plains Technology Center
AI Platform Control Workstation

Purpose
-------

This computer provides the user interface and control layer
for the GPTC AI Platform.

This machine connects to the GPU Server and provides:

Chat UI
RAG system
Workflow builder
Policy assistant
Teacher assistant
Code assistant
Database
Reverse proxy
User access

Hardware

Controller PC

64GB RAM
RTX 5090 GPU
NVMe storage
1Gb or 10Gb network

This machine may run small models locally,
but large models run on the GPU Server.

System Layout
-------------

/AI-CONTROLLER/

  /apps/
      /open-webui/
      /dify/
      /docling/
      /keycloak/
      /nginx/
      /postgres/

  /rag/
      /documents/
      /processed/
      /embeddings/

  /docker/
      /compose/
      /configs/
      /volumes/

  /logs/
      /webui/
      /dify/
      /proxy/

  /config/
      /env/
      /ssl/
      /users/

  /backups/
      /db/
      /rag/
      /configs/

Software Stack
--------------

Core

Docker
Docker Compose
PostgreSQL
pgvector
Open WebUI
Dify
Docling
Caddy / Nginx
Keycloak (optional)

Connection to GPU Server

vLLM API
Embeddings API
JupyterHub
MinIO

Models on Controller

Optional small models

Qwen 14B
Phi-3
Mistral 7B

Grant Compliance
----------------

Controller provides required systems for:

✔ User access
✔ Workflow tools
✔ AI assistants
✔ Policy lookup
✔ Instructor tools
✔ Data processing

Grant language requires both compute and instructional tools.
This machine provides the instructional layer.

Security Policy
---------------

Students do not have admin access.

All services run in Docker.

All traffic routed through reverse proxy.

Backups
-------

Database backed up daily
Configs backed up weekly
RAG docs backed up weekly

Administrator Notes
-------------------

All services run from /AI-CONTROLLER/docker

Do not install services outside containers unless required.