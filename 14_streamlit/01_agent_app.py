# 15. Level 13 – Streamlit AI agent application

# Install: pip install streamlit
### Code 35: Build an AI agent interface
# Create `14_streamlit/01_agent_app.py`.

import streamlit as st
from langchain_ollama import ChatOllama

st.set_page_config(page_title="My Agentic AI", page_icon="🤖")
st.title("My Agentic AI Assistant")
llm = ChatOllama(model="llama3.2:3b")
if "messages" not in st.session_state:
    st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            question = st.chat_input("Ask your AI agent")
            if question:
                st.session_state.messages.append({"role": "user", "content": question})
                with st.chat_message("user"):
                    st.write(question)
                    response = llm.invoke(question)


# Run: streamlit run 14_streamlit/01_agent_app.py


# This is a chatbot interface.
# Your next task is to connect your LangGraph workflow and tools to it.
