### Code 37: Basic Docker configuration

# Create `15_deployment/Dockerfile`.

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "13_fastapi.01_agent_api:app", "--host", "0.0.0.0", "--port", "8000"]


# For a Docker deployment, 
# the Ollama server must be accessible to the container.
# Do not assume `localhost` inside the container points to your Windows host.
