```markdown
# 🚀 Complete Agentic AI Coding Roadmap – Beginner to Advanced

A practical, hands-on engineering roadmap taking you from Python fundamentals to real-world autonomous AI agents, multi-agent systems, Model Context Protocol (MCP), and production deployment—running **100% locally** without paid APIs.

---

## 🎯 Course Objective

The goal is not just to understand Agentic AI conceptually, but to:
- **Architect and build** end-to-end agentic systems from scratch.
- **Explain system design** and trade-offs clearly in technical interviews.
- **Write clean, independent code** without relying on black-box abstractions.
- **Ship portfolio-ready projects** to GitHub.

---

## 🛠️ Local Development Stack

| Component | Specification | Purpose |
| :--- | :--- | :--- |
| **OS & Terminal** | Windows 11 + PowerShell | Local execution environment |
| **IDE** | Visual Studio Code | Code editing and integrated terminal |
| **Language** | Python 3.10 | Core development runtime |
| **Local LLM Runtime** | Ollama (`qwen3:4b`, `nomic-embed-text`) | Zero-cost local inference & embeddings |
| **Agent Frameworks** | LangChain & LangGraph | Orchestration, tool calling, and stateful workflows |
| **Backend & UI** | FastAPI & Streamlit | Production APIs and interactive web interfaces |

---

## 📚 Table of Contents

1. [Complete Agentic AI Syllabus](#1-complete-agentic-ai-syllabus)
2. [Workspace & Environment Setup](#2-workspace--environment-setup)
3. [Level 1 – Python Fundamentals for Agents](#3-level-1--python-fundamentals-for-agents)
4. [Level 2 – Local LLM Integration](#4-level-2--local-llm-integration)
5. [Level 3 – Your First Tool-Using AI Agent](#5-level-3--your-first-tool-using-ai-agent)
6. [Level 4 – Short-Term & Long-Term Agent Memory](#6-level-4--short-term--long-term-agent-memory)
7. [Level 5 – Planning, Reasoning & ReAct Agents](#7-level-5--planning-reasoning--react-agents)
8. [Level 6 – LangChain Agent Development](#8-level-6--langchain-agent-development)
9. [Level 7 – Stateful Workflows with LangGraph](#9-level-7--stateful-workflows-with-langgraph)
10. [Level 8 – RAG-Powered AI Agents](#10-level-8--rag-powered-ai-agents)
11. [Level 9 – Multi-Agent Systems](#11-level-9--multi-agent-systems)
12. [Level 10 – Model Context Protocol (MCP)](#12-level-10--model-context-protocol-mcp)
13. [Level 11 – Advanced Agentic AI Engineering](#13-level-11--advanced-agentic-ai-engineering)

---

## 1. Complete Agentic AI Syllabus

**Learning Journey:** `Beginner` ➔ `Intermediate` ➔ `Advanced` ➔ `Production`

1. **Python for AI Agents:** Functions, classes, OOP, JSON, APIs, exception handling, and asynchronous programming.
2. **LLM Fundamentals:** Prompts, tokens, temperature, context windows, and structured outputs.
3. **Building Your First AI Agent:** LLM + system instructions + reasoning loop + actions.
4. **Tools & Function Calling:** Calculator, web search, Python execution, SQL queries, and file operations.
5. **Agent Memory:** Short-term conversation history and persistent long-term memory with SQLite.
6. **Planning & Reasoning:** Task decomposition, ReAct loops, reflection, retries, and self-correction.
7. **LangChain:** Models, prompt templates, tools, tool binding, and runnable chains.
8. **LangGraph:** `StateGraph`, nodes, edges, conditional routing, cycles/loops, and checkpoints.
9. **RAG Agents:** PDF/CSV/Excel ingestion, chunking, embeddings, FAISS vector search, and citations.
10. **Multi-Agent Systems:** Supervisor, hierarchical, sequential, and parallel specialist agents.
11. **Model Context Protocol (MCP):** MCP architecture, servers, clients, tools, and resources.
12. **Advanced Agent Engineering:** Human-in-the-loop approval, guardrails, security, retries, and evaluations.
13. **Production Deployment:** FastAPI, Streamlit, Docker, logging, monitoring, and testing.

---

## 2. Workspace & Environment Setup

### Step 1: Create Project Directory Structure
Open VS Code Terminal (PowerShell) and run:

```powershell
cd $HOME\Desktop
mkdir Agentic_AI_Complete_Course
cd Agentic_AI_Complete_Course

mkdir 01_python_basics, 02_llm_basics, 03_first_agent, 04_agent_tools, `
      05_agent_memory, 06_agent_planning, 07_langchain, 08_langgraph, `
      09_rag_agents, 10_multi_agent, 11_mcp, 12_advanced_agents, `
      13_fastapi, 14_streamlit, 15_deployment, 16_projects

```

### Step 2: Set Up Python Virtual Environment & Dependencies

```powershell
py -3.10 -m venv venv
.\venv\Scripts\Activate.ps1
python --version

python -m pip install --upgrade pip
pip install ollama requests python-dotenv pydantic

```

> **Tip:** Add `venv/` to your `.gitignore` file immediately so you never commit large virtual environment binaries to GitHub.

### Step 3: Verify Ollama & Pull Local Models

```powershell
ollama list
ollama pull qwen3:4b
ollama run qwen3:4b

```

---

## 3. Level 1 – Python Fundamentals for Agents

Learn how an agent receives input, processes logic, maintains state, and returns an action.

### Code 1: Rule-Based Simple Agent

Create `01_python_basics/01_simple_agent.py`:

```python
def agent(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you?"
    elif "weather" in user_input.lower():
        return "I can help you check weather information."
    elif "python" in user_input.lower():
        return "Python is used to build AI agents."
    else:
        return "I don't know that yet."

while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("Agent: Goodbye!")
        break
    response = agent(question)
    print("Agent:", response)

```

Run:

```powershell
python 01_python_basics/01_simple_agent.py

```

> *Note: This is a deterministic rule-based agent, not yet an LLM-powered autonomous agent.*

### Code 2: Modular Agent Using Functions

Create `01_python_basics/02_agent_functions.py`:

```python
def greet():
    return "Hello! Welcome to Agentic AI."

def calculate():
    a = 10
    b = 20
    return a + b

def get_information():
    return "Agentic AI combines LLMs with tools and actions."

def agent(task):
    if task == "greet":
        return greet()
    elif task == "calculate":
        return calculate()
    elif task == "information":
        return get_information()
    return "Unknown task"

print(agent("greet"))
print(agent("calculate"))
print(agent("information"))

```

### Code 3: Object-Oriented Agent with State

Create `01_python_basics/03_agent_class.py`:

```python
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

```

**Concepts to Master:** Functions, classes, objects, lists, dictionaries, loops, exception handling, JSON parsing, and REST APIs.

---

## 4. Level 2 – Local LLM Integration

Connect Python directly to your local `qwen3:4b` model via Ollama.

### Code 4: First Local LLM Call

Create `02_llm_basics/01_local_llm.py`:

```python
import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain Agentic AI in simple words."
        }
    ]
)

print(response["message"]["content"])

```

### Code 5: Multi-Turn Interactive Chatbot

Create `02_llm_basics/02_chatbot.py`:

```python
import ollama

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

while True:
    question = input("\nYou: ")
    if question.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": question
    })

    response = ollama.chat(
        model="qwen3:4b",
        messages=messages
    )

    answer = response["message"]["content"]
    print("\nAI:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })

```

### Code 6: System Prompt Engineering

Create `02_llm_basics/03_prompt_engineering.py`:

```python
import ollama

system_prompt = """
You are an expert Agentic AI teacher.
Rules:
1. Explain concepts simply.
2. Give practical examples.
3. Explain why a concept is important.
4. Give Python code when required.
"""

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "Explain AI agent tools."
        }
    ]
)

print(response["message"]["content"])

```

**Core LLM Concepts:** System vs. user prompts, context windows & tokens, temperature & sampling, structured JSON outputs, hallucinations, and tool calling.

---

## 5. Level 3 – Your First Tool-Using AI Agent

An autonomous agent follows a core execution cycle:

```text
User Input ──▶ LLM (Understand & Decide) ──▶ Tools (Execute Action) ──▶ Observe Result ──▶ Final Answer

```

### Code 7: Single-Tool Routing Agent

Create `03_first_agent/01_tool_agent.py`:

```python
import ollama

def calculator(expression):
    allowed = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b
    }
    operation, a, b = expression
    if operation not in allowed:
        return "Unsupported operation"
    return allowed[operation](a, b)

def search_information(query):
    return f"Search requested for: {query}"

def agent(question):
    print("Agent thinking...")
    if "add" in question.lower():
        result = calculator(("add", 20, 30))
        return f"Calculator result: {result}"
    elif "search" in question.lower():
        return search_information(question)
    else:
        response = ollama.chat(
            model="qwen3:4b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response["message"]["content"]

while True:
    question = input("\nYou: ")
    if question.lower() == "exit":
        break
    print("Agent:", agent(question))

```

### Code 8: Multi-Tool Dispatching

Create `04_agent_tools/01_multiple_tools.py`:

```python
import ollama

def calculator(a, b):
    return a + b

def get_weather(city):
    return f"Weather lookup requested for {city}"

def get_database_info():
    return "Database contains employee records."

tools = {
    "calculator": calculator,
    "weather": get_weather,
    "database": get_database_info
}

def agent(task):
    task = task.lower()
    if "calculate" in task:
        return tools["calculator"](100, 200)
    elif "weather" in task:
        return tools["weather"]("Hyderabad")
    elif "database" in task:
        return tools["database"]()
    return ollama.chat(
        model="qwen3:4b",
        messages=[{"role": "user", "content": task}]
    )["message"]["content"]

print(agent("calculate"))
print(agent("check weather"))
print(agent("database"))

```

#### Essential Agent Toolset

| Tool | Purpose |
| --- | --- |
| **Calculator** | Exact mathematical operations |
| **Web Search** | Real-time external information |
| **SQL Tool** | Structured database querying |
| **Python Tool** | Data analysis and computation |
| **File Tool** | Reading PDF, CSV, and Excel documents |
| **API Tool** | Integrating third-party services |
| **Email / Calendar** | Workflow automation and scheduling |

> ⚠️ **Security Best Practice:** Never give an LLM unrestricted Python execution, SQL write permissions, or raw shell access. Enforce strict allowlists, input validation, and human approval gates for sensitive actions.

---

## 6. Level 4 – Short-Term & Long-Term Agent Memory

### Code 9: Sliding-Window Short-Term Memory

Create `05_agent_memory/01_short_term_memory.py`:

```python
import ollama

history = []

while True:
    question = input("\nYou: ")
    if question.lower() == "exit":
        break

    history.append({
        "role": "user",
        "content": question
    })

    response = ollama.chat(
        model="qwen3:4b",
        messages=history[-10:]  # Keep last 10 messages in context
    )

    answer = response["message"]["content"]
    print("\nAI:", answer)

    history.append({
        "role": "assistant",
        "content": answer
    })

```

### Code 10: Persistent Long-Term Memory (SQLite)

Create `05_agent_memory/02_long_term_memory.py`:

```python
import sqlite3

connection = sqlite3.connect("agent_memory.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    information TEXT
)
""")

def save_memory(info):
    cursor.execute(
        "INSERT INTO memories (information) VALUES (?)",
        (info,)
    )
    connection.commit()

def read_memory():
    cursor.execute("SELECT information FROM memories")
    return cursor.fetchall()

save_memory("My name is Taqhi")
save_memory("I am learning Agentic AI")
print(read_memory())

connection.close()

```

**Memory Architecture Topics:** Conversation buffer memory, persistent SQL storage, episodic vs. semantic memory, vector memory, summarization, and data privacy/expiration.

---

## 7. Level 5 – Planning, Reasoning & ReAct Agents

### Code 11: Task Decomposition Planner

Create `06_agent_planning/01_task_planner.py`:

```python
import ollama

def create_plan(task):
    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": """
                You are a task planning agent.
                Break tasks into small numbered steps.
                Do not execute them.
                """
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )
    return response["message"]["content"]

task = "Build a PDF question answering application"
plan = create_plan(task)
print("Generated Plan:\n", plan)

```

### Code 12: Self-Reflection Agent

Create `06_agent_planning/02_reflection_agent.py`:

```python
import ollama

def ask_llm(prompt):
    result = ollama.chat(
        model="qwen3:4b",
        messages=[{"role": "user", "content": prompt}]
    )
    return result["message"]["content"]

task = "Explain LangGraph"
draft = ask_llm(task)
review = ask_llm("Review this answer and identify mistakes:\n" + draft)
improved = ask_llm(
    "Improve this answer using the review:\n" + review +
    "\nOriginal answer:\n" + draft
)

print("Original:\n", draft)
print("\nReview:\n", review)
print("\nImproved:\n", improved)

```

### Code 13: ReAct-Style Agent (Reason + Act + Observe)

Create `06_agent_planning/03_react_agent.py`:

```python
import ollama

def calculator(a, b):
    return a + b

def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": """
            You are an AI assistant.
            Explain the steps needed to solve the user's task.
            Never claim to have executed a tool unless it actually ran.
            """
        },
        {
            "role": "user",
            "content": question
        }
    ]
    response = ollama.chat(
        model="qwen3:4b",
        messages=messages
    )
    print("Reasoning/plan:\n", response["message"]["content"])
    observation = calculator(10, 20)
    print("Tool observation:", observation)

run_agent("Add 10 and 20")

```

---

## 8. Level 6 – LangChain Agent Development

Transition from raw Python wrappers to standardized orchestration primitives.

```powershell
pip install langchain langchain-core langchain-ollama

```

### Code 14: LangChain + Ollama Integration

Create `07_langchain/01_langchain_llm.py`:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b", temperature=0)
response = llm.invoke("Explain the difference between AI and Agentic AI")
print(response.content)

```

### Code 15: LCEL Prompt Templates & Chains

Create `07_langchain/02_prompt_template.py`:

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="qwen3:4b")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an Agentic AI expert."),
    ("human", "Explain {topic} with Python examples.")
])

chain = prompt | llm
result = chain.invoke({"topic": "AI Agent Tools"})
print(result.content)

```

### Code 16: Structured Tool Binding

Create `07_langchain/03_langchain_tools.py`:

```python
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

llm = ChatOllama(model="qwen3:4b", temperature=0)
llm_with_tools = llm.bind_tools([add_numbers, multiply_numbers])

response = llm_with_tools.invoke("What is 25 multiplied by 4?")
print(response.tool_calls)

```

> *Note: `bind_tools` generates structured tool call payloads; execution loops are handled in LangGraph.*

---

## 9. Level 7 – Stateful Workflows with LangGraph

> ⭐ **High-Priority Interview Skill:** LangGraph enables cyclic, stateful, controllable agent execution graphs.

```powershell
pip install langgraph langchain-ollama

```

### Code 17: Minimal StateGraph

Create `08_langgraph/01_first_graph.py`:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    question: str
    answer: str

def assistant(state: AgentState):
    return {"answer": "You asked: " + state["question"]}

builder = StateGraph(AgentState)
builder.add_node("assistant", assistant)
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)

graph = builder.compile()
result = graph.invoke({"question": "What is LangGraph?", "answer": ""})
print(result["answer"])

```

### Code 18: LangGraph with LLM Node

Create `08_langgraph/02_llm_graph.py`:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b")

class AgentState(TypedDict):
    question: str
    answer: str

def ai_agent(state: AgentState):
    response = llm.invoke(state["question"])
    return {"answer": response.content}

builder = StateGraph(AgentState)
builder.add_node("ai_agent", ai_agent)
builder.add_edge(START, "ai_agent")
builder.add_edge("ai_agent", END)

graph = builder.compile()
result = graph.invoke({"question": "What is an autonomous AI agent?", "answer": ""})
print(result["answer"])

```

### Code 19: Conditional Routing

Create `08_langgraph/03_conditional_graph.py`:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    question: str
    category: str
    answer: str

def classify(state: State):
    question = state["question"].lower()
    if "python" in question:
        category = "python"
    elif "sql" in question:
        category = "sql"
    else:
        category = "general"
    return {"category": category}

def python_agent(state: State):
    return {"answer": "This is a Python-related question."}

def sql_agent(state: State):
    return {"answer": "This is a SQL-related question."}

def general_agent(state: State):
    return {"answer": "This is a general question."}

def route_question(state: State):
    return state["category"]

builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("python", python_agent)
builder.add_node("sql", sql_agent)
builder.add_node("general", general_agent)

builder.add_edge(START, "classify")
builder.add_conditional_edges(
    "classify",
    route_question,
    {"python": "python", "sql": "sql", "general": "general"}
)
builder.add_edge("python", END)
builder.add_edge("sql", END)
builder.add_edge("general", END)

graph = builder.compile()
print(graph.invoke({"question": "How do I write a SQL join?", "category": "", "answer": ""}))

```

### Code 20: Cyclic Loops

Create `08_langgraph/04_agent_loop.py`:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    count: int

def increment(state: State):
    return {"count": state["count"] + 1}

def continue_loop(state: State):
    if state["count"] < 5:
        return "increment"
    return "finish"

builder = StateGraph(State)
builder.add_node("increment", increment)
builder.add_edge(START, "increment")
builder.add_conditional_edges(
    "increment",
    continue_loop,
    {
        "increment": "increment",
        "finish": END
    }
)

graph = builder.compile()
print(graph.invoke({"count": 0}))  # Output: {'count': 5}

```

### Code 21: Human-in-the-Loop Approval

Create `08_langgraph/05_human_approval.py`:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

class State(TypedDict):
    action: str
    approval: str

def approval_node(state: State):
    decision = interrupt(f"Approve this action? {state['action']}")
    return {"approval": decision}

def execute_node(state: State):
    if state["approval"] == "yes":
        return {"approval": "Approved and executed"}
    return {"approval": "Rejected; not executed"}

builder = StateGraph(State)
builder.add_node("approval", approval_node)
builder.add_node("execute", execute_node)
builder.add_edge(START, "approval")
builder.add_edge("approval", "execute")
builder.add_edge("execute", END)

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

```

---

## 10. Level 8 – RAG-Powered AI Agents

Ground your agents in private documents using local embeddings and FAISS vector search.

```powershell
pip install pypdf faiss-cpu sentence-transformers langchain-community langchain-text-splitters
ollama pull nomic-embed-text

```

### Code 22: PDF Text Extraction

Create `09_rag_agents/01_pdf_loader.py` (place a `sample.pdf` in `09_rag_agents/`):

```python
from pypdf import PdfReader

reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() or ""

print(text)

```

### Code 23: Recursive Text Chunking

Create `09_rag_agents/02_text_splitter.py`:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Agentic AI is a technology where AI agents
can reason, use tools and complete tasks."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)
for chunk in chunks:
    print(chunk)
    print("-" * 16)

```

### Code 24: Local FAISS Vector Store

Create `09_rag_agents/03_faiss_database.py`:

```python
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

documents = [
    "LangGraph is used to create stateful AI workflows.",
    "LangChain helps developers connect LLMs with tools.",
    "RAG retrieves relevant information from documents."
]

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_texts(documents, embedding=embeddings)
vectorstore.save_local("faiss_index")

results = vectorstore.similarity_search("What is LangGraph?", k=2)
for result in results:
    print(result.page_content)

```

### Code 25: Grounded RAG Question-Answering

Create `09_rag_agents/04_rag_qa.py`:

```python
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True  # Only load trusted local indexes
)

llm = ChatOllama(model="qwen3:4b")
question = input("Ask a question: ")

docs = vectorstore.similarity_search(question, k=3)
context = "\n".join(doc.page_content for doc in docs)

prompt = f"""Answer only using the following context.

Context:
{context}

Question:
{question}"""

answer = llm.invoke(prompt)
print(answer.content)

```

### Code 26: Agentic RAG Architecture (Self-Correcting Retrieval)

```text
User Question
      │
      ▼
Query Analyzer
      │
      ▼
  Retriever
      │
      ▼
Document Evaluator
      │
      ├─── Relevant? ── No ──▶ Rewrite Query ──▶ Retrieve Again (with max retry cap)
      │
     Yes
      │
      ▼
LLM Answer Generator
      │
      ▼
Citation Checker
      │
      ▼
 Final Answer

```

---

## 11. Level 9 – Multi-Agent Systems

Coordinate specialized agents using sequential pipelines, supervisor routing, and parallel execution.

### Code 27: Sequential Researcher + Writer Pipeline

Create `10_multi_agent/01_two_agents.py`:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b")

def researcher(topic):
    prompt = f"""
    You are a research agent.
    Explain the important facts about: {topic}
    """
    return llm.invoke(prompt).content

def writer(research):
    prompt = f"""
    You are a technical writer.
    Create a clear explanation from this research:
    {research}
    """
    return llm.invoke(prompt).content

topic = "Agentic AI"
research = researcher(topic)
article = writer(research)

print("Research:\n", research)
print("\nArticle:\n", article)

```

### Code 28: Supervisor Routing Agent

Create `10_multi_agent/02_supervisor.py`:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b")

def researcher(task):
    return "Research completed for: " + task

def coder(task):
    return "Code generation requested for: " + task

def analyst(task):
    return "Analysis completed for: " + task

def supervisor(task):
    prompt = f"""
    Choose one specialist for this task.
    Available specialists: researcher, coder, analyst
    Task: {task}
    Return only the specialist name.
    """
    response = llm.invoke(prompt)
    choice = response.content.strip().lower()
    agents = {"researcher": researcher, "coder": coder, "analyst": analyst}
    return agents.get(choice, researcher)(task)

print(supervisor("Write a Python function to parse JSON"))

```

### Code 29: Parallel Agent Execution

Create `10_multi_agent/03_parallel_agents.py`:

```python
from concurrent.futures import ThreadPoolExecutor
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b")

def run_agent(role, task):
    prompt = f"""
    You are a {role}.
    Complete this task: {task}
    """
    return role, llm.invoke(prompt).content

task = "Explain Agentic AI applications"
roles = ["researcher", "analyst"]

with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(run_agent, role, task) for role in roles]
    for future in futures:
        role, result = future.result()
        print(f"\n[{role.upper()}]\n{result}")

```

> **Hardware Note:** On 8 GB RAM machines, keep `max_workers=1` or run sequentially first, as concurrent local LLM inference increases memory pressure.

---

## 12. Level 10 – Model Context Protocol (MCP)

Standardize how AI applications discover and invoke external tools and resources.

```powershell
pip install "mcp[cli]"

```

### Code 30: Build an MCP Server

Create `11_mcp/01_mcp_server.py`:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyFirstMCPServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Greet a user."""
    return f"Hello {name}"

if __name__ == "__main__":
    mcp.run(transport="stdio")

```

### Code 31: Build an MCP Client

Create `11_mcp/02_mcp_client.py`:

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server = StdioServerParameters(
        command="python",
        args=["11_mcp/01_mcp_server.py"]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print("-", tool.name)

            result = await session.call_tool(
                "add",
                arguments={"a": 10, "b": 20}
            )
            print("Result:", result.content)

asyncio.run(main())

```

Run from the root directory:

```powershell
python 11_mcp/02_mcp_client.py

```

---

## 13. Level 11 – Advanced Agentic AI Engineering

Master these production engineering patterns to transition from prototype developer to Senior Agentic AI Engineer:

| Concept | Practical Implementation |
| --- | --- |
| **Tool Calling** | JSON-schema dynamic tool invocation |
| **ReAct** | Autonomous Reason-Act-Observe loops |
| **Reflection** | Self-critique and iterative refinement |
| **Planning** | Multi-step task decomposition |
| **Routing** | Semantic and LLM-based intent routing |
| **Handoffs** | State transfer between specialist agents |
| **Checkpointing** | Saving and resuming graph execution state |
| **Persistence** | Durable storage with SQLite / PostgreSQL |
| **Human-in-the-Loop** | Interrupts and approval gates before critical actions |
| **Guardrails** | Input sanitization and structured output validation |
| **Retry Mechanism** | Exponential backoff for transient failures |
| **Fallback Models** | Graceful degradation across local/cloud models |
| **Parallel Execution** | Concurrent fan-out/fan-in agent workflows |
| **Agent Evaluation** | Automated accuracy, faithfulness, and tool-use benchmarks |
| **Observability** | Step-by-step execution tracing and latency profiling |
| **Cost & Token Tracking** | Monitoring context size and token throughput |
| **MCP** | Standardized tool/resource servers and clients |
| **Sandboxing** | Isolated execution environments for generated code |

```

```
