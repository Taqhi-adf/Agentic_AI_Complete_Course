### Code 6: Understand prompt engineering

# Create `02_llm_basics/03_prompt_engineering.py`.

import ollama

system_prompt = """You are an expert Agentic AI teacher.
Rules:
1. Explain concepts simply.
2. Give practical examples.
3. Explain why a concept is important.
4. Give Python code when required."""
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Explain AI agent tools."},
    ],
)
print(response["message"]["content"])


# Learn these LLM concepts:

# - System prompts and user prompts.
# - Context windows and tokens.
# - Temperature and sampling.
# - JSON/structured outputs.
# - Model hallucinations.
# - Context management.
# - LLM tool calling.
