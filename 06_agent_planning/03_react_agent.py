### Code 13: ReAct-style agent

# ReAct means Reasoning + Acting + Observation.

# Create `06_agent_planning/03_react_agent.py`.

import ollama


def calculator(a, b):
    return a + b


def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": """You are an AI assistant.            
                 Explain the steps needed to solve the user's task.            
                 Never claim to have executed a tool unless it actually ran. """,
        },
        {"role": "user", "content": question},
    ]
    response = ollama.chat(model="llama3.2:3b", messages=messages)
    print("Reasoning/plan:")
    print(response["message"]["content"])
    observation = calculator(10, 20)
    print("Tool observation:", observation)


# This is a simplified ReAct demonstration, not a complete autonomous ReAct loop.
# The next step is to connect the model's structured action selection to real tools,
# execute only validated actions, and feed observations back until the agent finishes
# or reaches a step limit.
