# 13. Level 11 – Advanced Agentic AI concepts

# These are the topics that help you move from a
# basic AI developer to an advanced Agentic AI engineer.

# | Concept            | Practical coding exercise   |
# | ------------------ | --------------------------- |
# | Tool calling       | JSON-based dynamic tools    |
# | ReAct              | Reason and act loop         |
# | Reflection         | Self-review agent           |
# | Planning           | Multi-step task planner     |
# | Routing            | Intelligent task routing    |
# | Handoffs           | Transfer between agents     |
# | Checkpointing      | Save agent state            |
# | Persistence        | SQLite/PostgreSQL           |
# | Human-in-the-loop  | Approval before actions     |
# | Guardrails         | Validate inputs and outputs |
# | Retry mechanism    | Retry failed operations     |
# | Fallback models    | Switch models on failure    |
# | Parallel execution | Run independent agents      |
# | Agent evaluation   | Test agent accuracy         |
# | Observability      | Trace agent execution       |
# | Cost tracking      | Monitor token usage         |
# | MCP                | Connect external tools      |
# | Sandboxing         | Isolate code execution      |
# | Authentication     | Secure agent APIs           |
# | Rate limiting      | Control API requests        |

### Code 32: Agent retry mechanism

# Create `12_advanced_agents/01_retry_agent.py`.

import time


def unreliable_task():
    raise ValueError("Temporary failure")


def execute_with_retry(max_retries=3):
    for attempt in range(max_retries):
        try:
            return unreliable_task()
        except Exception as error:
            print("Attempt failed:", attempt + 1)
            if attempt == max_retries - 1:
                raise time.sleep(1)
            try:
                execute_with_retry()
            except Exception as error:
                print("Final failure:", error)
