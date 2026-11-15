#  Level 6 – LangChain Agent Development

# Now move from plain Python agents to industry frameworks.
# Install: pip install langchain langchain-core langchain-ollama

### Code 14: Connect LangChain with Ollama

# Create `07_langchain/01_langchain_llm.py`.

from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:3b", temperature=0)
response = llm.invoke("Explain the difference between AI and Agentic AI")
print(response.content)
