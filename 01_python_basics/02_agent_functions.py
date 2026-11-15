### Code 2: Agent using Python functions
# Create `01_python_basics/02_agent_functions.py`.


def greet():
    return "Hello! Welcome to Agentic AI."


def calculate():
    a = 10
    b = 20
    return a + b


def get_information():
    return "Agentic AI combines LLMs with tools and actions."


def agent(task):
    if task == "greet":
        return greet()
    elif task == "calculate":
        return calculate()
    elif task == "information":
        return get_information()
    return "Unknown task"


print(agent("greet"))
print(agent("calculate"))
print(agent("information"))
