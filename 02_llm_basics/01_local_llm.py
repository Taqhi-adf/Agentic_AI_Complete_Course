# Level 2 – LLM integration (First local LLM application)
# Now connect Python to your local Qwen3 model.
# Install: pip install ollama
# Create `02_llm_basics/01_local_llm.py`.
import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "Explain Agentic AI in simple words."}],
)
print(response["message"]["content"])

# Run:``` python 02_llm_basics/01_local_llm.py
