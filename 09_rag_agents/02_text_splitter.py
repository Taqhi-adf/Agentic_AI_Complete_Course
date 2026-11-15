### Code 23: Split text into chunks

# Create `09_rag_agents/02_text_splitter.py`.
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Agentic AI is a technology where AI agentscan reason, 
use tools and complete tasks."""
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
chunks = splitter.split_text(text)
for chunk in chunks:
    print(chunk)
    print("----------------")


# Install the additional package: pip install langchain-text-splitters
