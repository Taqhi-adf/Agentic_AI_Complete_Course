### Code 24: Create a FAISS vector database

# Create `09_rag_agents/03_faiss_database.py`.
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

documents = [
    "LangGraph is used to create stateful AI workflows.",
    "LangChain helps developers connect LLMs with tools.",
    "RAG retrieves relevant information from documents.",
]
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_texts(documents, embedding=embeddings)
vectorstore.save_local("faiss_index")
results = vectorstore.similarity_search("What is LangGraph?", k=3)
for result in results:
    print(result.page_content)


# First install the embedding model: ollama pull nomic-embed-text
