AI PLATFORM GPU SERVER
Great Plains Technology Center
AI / Cybersecurity / Data Science Compute Node

Purpose
-------
This server provides centralized GPU compute resources for the GPTC AI Platform,
funded through the HGET Innovative Grant. The system supports instruction in:

- Artificial Intelligence
- Machine Learning
- Cybersecurity
- Data Science
- Database / Cloud Computing
- High Performance Computing

Hardware
--------
GPU Server:
3 × NVIDIA H100 80GB
1 × NVIDIA A40 48GB
High-core CPU
256GB+ RAM
High-speed NVMe storage
10Gb network connection

This server is NOT used as a workstation.
This server provides remote compute only.

System Layout
-------------

/AI-SERVER/

  /models/
      /llm/
      /embedding/
      /reranker/
      /quantized/

  /datasets/
      /cyber/
      /ai/
      /ml/
      /student/

  /docker/
      /vllm/
      /tei/
      /jupyter/
      /minio/
      /monitoring/

  /storage/
      /minio/
      /artifacts/
      /checkpoints/

  /logs/
      /docker/
      /models/
      /system/

  /config/
      /docker/
      /nginx/
      /env/

  /backups/
      /models/
      /configs/
      /datasets/

Software Stack
--------------

Core

Docker
Docker Compose
NVIDIA Container Toolkit
CUDA
vLLM
Text Embeddings Inference
JupyterHub
PyTorch
TensorFlow
MinIO

Models

Qwen2.5-Coder-32B
DeepSeek-R1-Distill-32B
Llama-3.3-70B (optional)
bge-m3
bge-reranker

Usage Policy
------------

Students do not log into the server directly.

Access is provided through:

Controller PC
WebUI
JupyterHub
API endpoints

Grant Compliance
----------------

This server fulfills grant requirements for:

✔ AI instruction
✔ Machine learning
✔ Cybersecurity training
✔ Data science
✔ Database systems
✔ High performance computing
✔ Virtual lab environments

All compute workloads are centralized here.

Backup Policy
-------------

Models backed up weekly
Configs backed up daily
Datasets backed up monthly

Do not store personal files on server.

Administrator Notes
-------------------

All containers run from /AI-SERVER/docker

All models stored in /AI-SERVER/models

Do not install software outside Docker unless required.