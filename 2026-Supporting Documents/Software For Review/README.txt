GPTC compose starter pack

Files included:
- AI-SERVER/apps/vllm-coder/docker-compose.yml
- AI-SERVER/apps/vllm-reasoning/docker-compose.yml
- AI-SERVER/apps/tei-embeddings/docker-compose.yml
- AI-SERVER/apps/jupyterhub/docker-compose.yml
- AI-SERVER/apps/jupyterhub/jupyterhub_config.py
- AI-CONTROLLER/apps/stack/docker-compose.yml
- AI-CONTROLLER/apps/stack/.env.example
- AI-CONTROLLER/apps/stack/Caddyfile
- AI-CONTROLLER/apps/dify/docker-compose.yml
- AI-CONTROLLER/apps/dify/.env.example

Notes:
- These are starter files, not a final production hardening package.
- Update all CHANGE_ME values before running.
- Create the required host folders before docker compose up -d.
- Replace DummyAuthenticator in JupyterHub before production.
- Dify is the most likely file to need adjustment because its upstream environment matrix changes often.
