### Code 3: Learn Python OOP for agents
# Create `01_python_basics/03_agent_class.py`.


class AIAgent:
    def __init__(self, name):
        self.name = name
        self.memory = []

    def think(self, question):
        self.memory.append(question)
        return f"{self.name} received: {question}"

    def show_memory(self):
        return self.memory


agent = AIAgent("MyFirstAgent")
print(agent.think("What is Agentic AI?"))
print(agent.think("What is LangGraph?"))
print(agent.show_memory())


# Concepts to master: functions, classes, objects, lists, dictionaries, loops, exception handling, JSON and APIs.
