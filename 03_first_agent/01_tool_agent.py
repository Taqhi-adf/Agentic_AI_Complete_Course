#  Level 3 – Build your first actual AI agent

# This is where Agentic AI starts becoming interesting.
# An AI agent generally contains:
# User input
# LLM – Understand and decide
# Tools – Perform actions
# Observe tool results
# Final answer

### Code 7: Create your first tool-using agent

# Create `03_first_agent/01_tool_agent.py`.

import ollama


def calculator(expression):
    allowed = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
    }
    operation, a, b = expression
    if operation not in allowed:
        return "Unsupported operation"
    return allowed[operation](a, b)


def search_information(query):
    return f"Search requested for: {query}"


def agent(question):
    print("Agent thinking...")
    if "add" in question.lower():
        result = calculator(("add", 20, 30))
        return f"Calculator result: {result}"
    elif "search" in question.lower():
        return search_information(question)
    else:
        response = ollama.chat(
            model="llama3.2:3b", messages=[{"role": "user", "content": question}]
        )
        return response["message"]["content"]
    while True:
        question = input("\nYou: ")
        if question.lower() == "exit":
            break
        print("Agent:", agent(question))


# Try:
# You: Add two numbers
# Agent: Calculator result: 50

# You: What is LangGraph?
# Agent: ...

# Notice that the first tool is currently hardcoded to add 20 and 30. Later, you will replace that logic with structured tool arguments selected by the LLM.
