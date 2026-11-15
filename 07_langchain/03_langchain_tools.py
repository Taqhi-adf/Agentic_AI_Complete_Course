### Code 16: LangChain tool calling

# Create `07_langchain/03_langchain_tools.py`.

from langchain_core.tools import tool
from langchain_ollama import ChatOllama


@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


llm = ChatOllama(model="llama3.2:3b", temperature=0)
llm_with_tools = llm.bind_tools([add_numbers, multiply_numbers])
response = llm_with_tools.invoke("What is 25 multiplied by 4?")
print(response.tool_calls)


# Important: This demonstrates tool-call generation.
# It does not automatically execute the returned tool calls.
# You will implement execution and observation in the LangGraph section.
# Check that your installed Ollama model supports tool calling.
