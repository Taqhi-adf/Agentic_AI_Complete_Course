#  Level 12 – Deploy agents using FastAPI

# An AI agent becomes more useful when other applications can access it through an API.

# Install: pip install fastapi uvicorn

### Code 34: Build an AI agent API

# Create `13_fastapi/01_agent_api.py`.

from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama

# Initialize FastAPI
app = FastAPI(title="My Agent API")

# Initialize Ollama LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0)


# Define request schema
class AgentRequest(BaseModel):
    question: str


# Home endpoint
@app.get("/")
def home():
    return {"status": "Agent API running"}


# Ask Agent endpoint
@app.post("/ask")
def ask_agent(request: AgentRequest):

    response = llm.invoke(request.question)

    return {"question": request.question, "answer": response.content}


# Run: uvicorn 13_fastapi.01_agent_api:app --reload

# Open: http://127.0.0.1:8000/docs
# You now have an API endpoint for your AI assistant.
