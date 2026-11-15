### Code 25: RAG question-answering application

# Create `09_rag_agents/04_rag_qa.py`.

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.load_local(
    "faiss_index", embeddings, allow_dangerous_deserialization=True
)
llm = ChatOllama(model="llama3.2:3b")
question = input("Ask a question: ")
docs = vectorstore.similarity_search(question, k=3)
context = "\n".join(doc.page_content for doc in docs)
prompt = f"""Answer only using the following context.
Context:{context}
Question:{question}"""
answer = llm.invoke(prompt)
print(answer.content)


# Only load FAISS indexes that you created or otherwise trust.
# Pickle-based deserialization can execute malicious code.
