### Code 10: Long-term memory using SQLite

# Create `05_agent_memory/02_long_term_memory.py`.

import sqlite3

connection = sqlite3.connect("agent_memory.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY AUTOINCREMENT,
               information TEXT)""")


def save_memory(info):
    cursor.execute("INSERT INTO memories (information) VALUES (?)", (info,))
    connection.commit()


def read_memory():
    cursor.execute("SELECT information FROM memories")
    return cursor.fetchall()


save_memory("My name is Taqhi")
save_memory("I am learning Agentic AI")
print(read_memory())
connection.close()


# Learn:

# - Conversation memory.
# - Persistent memory.
# - Episodic memory.
# - Semantic memory.
# - Vector memory.
# - Memory retrieval.
# - Memory summarization.
# - Memory expiration and privacy.
