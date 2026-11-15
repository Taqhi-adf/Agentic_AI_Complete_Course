#  Level 4 – Agent memory

# Agents need memory to remember previous interactions and important information.

### Code 9: Short-term memory

# Create `05_agent_memory/01_short_term_memory.py`.


import ollama

history = []
while True:
    question = input("\nYou: ")
    if question.lower() == "exit":
        break
    history.append({"role": "user", "content": question})
    response = ollama.chat(model="llama3.2:3b", messages=history[-10:])
    answer = response["message"]["content"]
    print("\nAI:", answer)
    history.append({"role": "assistant", "content": answer})
