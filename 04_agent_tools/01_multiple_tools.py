### Code 8: Multiple tools with tool selection
# Create `04_agent_tools/01_multiple_tools.py`.

import ollama


def calculator(a, b):
    return a + b


def get_weather(city):
    return f"Weather lookup requested for {city}"


def get_database_info():
    return "Database contains employee records."


tools = {
    "calculator": calculator,
    "weather": get_weather,
    "database": get_database_info,
}


def agent(task):
    task = task.lower()
    if "calculate" in task:
        return tools["calculator"](100, 200)
    elif "weather" in task:
        return tools["weather"]("Hyderabad")
    elif "database" in task:
        return tools["database"]()
    return ollama.chat(
        model="llama3.2:3b", messages=[{"role": "user", "content": task}]
    )["message"]["content"]


print(agent("calculate"))
print(agent("check weather"))
print(agent("database"))

# Master these tools:

# | Tool          | Why you need it          |
# | ------------- | ------------------------ |
# | Calculator    | Mathematical operations  |
# | Web search    | External information     |
# | SQL tool      | Database queries         |
# | Python tool   | Data analysis            |
# | File tool     | Read PDF, CSV, Excel     |
# | API tool      | Connect external systems |
# | Email tool    | Communication workflows  |
# | Calendar tool | Scheduling               |

# Important: Do not give an LLM unrestricted Python execution,
# SQL write access, or shell access. Use allowlisted tools,
# input validation, and approval for sensitive operations.
