### Code 5: Interactive chatbot

# Create `02_llm_basics/02_chatbot.py`.


import ollama

messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
while True:
    question = input("\nYou: ")
    if question.lower() == "exit":
        break
    messages.append({"role": "user", "content": question})
    response = ollama.chat(model="llama3.2:3b", messages=messages)
    answer = response["message"]["content"]
    print("\nAI:", answer)
    messages.append({"role": "assistant", "content": answer})
