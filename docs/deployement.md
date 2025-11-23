# Déploiement

## GPU local

```python
device_map="cuda:0"
```
## CPU
```python
device_map="cpu"
torch_dtype=torch.float32
```
## Docker
```Dockerfile
FROM python:3.9-slim
RUN pip install torch transformers accelerate
COPY app.py /app/app.py
CMD ["python", "/app/app.py"]
Déploiement sur serveur
Uvicorn + FastAPI
Docker compose
Traefik / Nginx
