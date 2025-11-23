FROM python:3.10-slim

WORKDIR /app

COPY . .

EXPOSE 4298

RUN pip install --no-cache-dir -r requirements.txt || true

CMD ["python3", "main.py", "python3", "app.py",]
