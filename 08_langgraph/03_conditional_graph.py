### Code 19: Conditional routing

# Create `08_langgraph/03_conditional_graph.py`.

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    question: str
    category: str
    answer: str

    def classify(state):
        question = state["question"].lower()
        if "python" in question:
            category = "python"
        elif "sql" in question:
            category = "sql"
        else:
            category = "general"
            return {"category": category}

        def python_agent(state):
            return {"answer": "This is a Python-related question."}

        def sql_agent(state):
            return {"answer": "This is a SQL-related question."}

        def general_agent(state):
            return {"answer": "This is a general question."}
