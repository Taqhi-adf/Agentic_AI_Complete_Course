# 7. Level 5 – Planning, reasoning and ReAct agents

### Code 11: Task planning agent

# Create `06_agent_planning/01_task_planner.py`.

import ollama


def create_plan(task):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": """You are a task planning agent.
                                      Break tasks into small numbered steps.                
                                      Do not execute them. """,
            },
            {"role": "user", "content": task},
        ],
    )
    return response["message"]["content"]


task = "Build a PDF question answering application"
plan = create_plan(task)
print("Generated Plan:")
print(plan)
