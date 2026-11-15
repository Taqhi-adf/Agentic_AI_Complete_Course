# 10. Level 8 – RAG-powered AI agents

# Build agents that understand your documents and answer questions from your own data.

# [Building RAG Chatbots: Bridging LLMs with Private Data | Rahul K B | Staff Machine Learning Engineer](https://images.openai.com/static-rsc-4/zee8MkIg-u9r2bPUM2aLGQO4-Otm_xxZ8OAIc8kMIT6YEUi4Lq6cYhbrXDXlrR1N6K2mxLZaNPQhlk6xcMKMihqDnRd47YZjqaHBDtIRuL1ja0jK5jt1zoFXJuSYUhITSgaM29PbwitMjBx5SS67x5X8lrQqc7-26o7REMCHYPU?purpose=inline)

# [How I choose between prompt engineering, RAG, and fine-tuning | by System Design with Sage | Medium](https://images.openai.com/static-rsc-4/0JfWbLRX5lrjOATEHKLrx-y5Hu7xpQwzqBR2kghb_OViA-D9dj0YjCjfgKubzbPhgNbtYgb7naij-ZhmGq0R4SETiMv968V-4aOtDFcf0zkXioEBbg965AjI71YVvdXeNrF1PG-7sb4Tlq2Ul5A4ieMTa-RQTvF2sx1Y6DVClR0?purpose=inline)

# [🔍 Exploring RAG with FAISS and OpenAI — all on Google Colab! | by Alexandr Dzhumurat | Medium](https://images.openai.com/static-rsc-4/G35naNIEpY_CBiqZ0zDpSswIQnkyhn7LiTJva8nT9KOcoupyHEI0ppxR_Y5_s5qwd43_SUFN3g29biiXEpf11tLlwkluCaKfizFYxbM0_QlXg4cSBNfmMhV111ip8XHVY9XCLC80kyXEFJ50w2ox6g5QimqZms77OXiCVUG_LmQ?purpose=inline)

# [Building a Semantic Search Backbone for an Intelligent RAG-Based Research Assistant | by Akanksha Sinha | Medium](https://images.openai.com/static-rsc-4/TkEyO30Ed7Vmh1L7kid_jdi_xLP_n_nEqFIjaVkoZcL8Ih6fzvcVFo2IHbjIHPsyvuxytQ6gAXz1ugwAbR0FJ0f2VfoHAeQhRUV5Q_EcfxZrrzKtkRYexvpVZRfZmtK-DSU4fzx6W8_kf86v3RjKUJcqTAMMmbtq0uZ9nKezq9w?purpose=inline)

# [AI Agents in Action, Second Edition](https://images.openai.com/static-rsc-4/o47tJTgR7KcccDbshm0TMtcS39vD0vFKuiRB-o6cFOl39PHo6fdwUJ0faMH0zKKnk9cqcUET0zjSjZttxeJhjlc2yrTxJ4r8LNryQeJPGub51IIlGLLmEbPewMsZ4IxVAHbgupnlJu7mjzQJm4JaHwHBK3tZ1WsLS0ZfohiCUo8?purpose=inline)

# [What is a Vector Database? Essential Guide for GenAI Developers](https://images.openai.com/static-rsc-4/QsI9v0agV3kw3yj4VD6cOLujOjf_o2E76xc0HFHWKi_DdlOMXSpzyWe6FtsVuTXezWWIz9tJZs1MJ_swuUgNRSWi_ZjbbzOkWyUmoe19I4tSAADQZjM6pmA92s_xNwn6pfECQPt4HJ4zHoBpGztakyd5EVNr96h4WeuO6q0FFqQ?purpose=inline)

# [Extracting Text from PDFs in Python Using pdfplumber (A Practical Guide) | by Arun C | Medium](https://images.openai.com/static-rsc-4/nwSnn4KOxBAirVa6oQZ65ZUXTk3Xa6QljQtyj_tPcWkfmVs13pDLadHdo6QztWCY5JnYYDdvos9mTmepSW_DveYs3GZ2nDDt36UpdVn8OulCpeVCJOwDL2NxMqPP7WCOguhZzSb8VKzypY-2up4XTNHG62kdH7zBDM0ZFhfGqS4?purpose=inline)

# [Building Q&A System using Agentic RAG with MuleSoft in the Center | by Sravan Nerella | Mar, 2026 | Medium](https://images.openai.com/static-rsc-4/4wcGXypJgkq28EvvnhUNKzAefjLIyC1PsjwFCXtsrjz2FubNtWpCAcUJ2l8wwOmw8j1e1jNwpJZpZJAXdhJC6BVziptm0ZWuB4AVt0ivnB96dNpTkXjFX3LpbgZtzAaNOFCUXYgBiyuA9eJEuYL8VGOzOrxic7LZi_AJ2yGfVzc?purpose=inline)

# [FAISS, HNSWlib, ScaNN: Pick the Right Search Index](https://images.openai.com/static-rsc-4/BUhSYN6iCjOSq18cSQh_Dlkk1X92aL5cInbS_QDoqai-emFVPu-T1QeoysgEAvt6klC7-VrZx16KKH2qef13anPSmUrLBNGIJA6n5NsvvJhGZoG9TfPnyuOE-SgibQlv5pcHv2fbPVV1KJ4KFdYcTJNDq5F8-u8e1z8oxQeywis?purpose=inline)

# Learn:
# - Document loaders.
# - PDF extraction.
# - Text splitting.
# - Chunking strategies.
# - Embeddings.
# - FAISS.
# - Vector similarity search.
# - Retriever.
# - RAG chains.
# - Agentic RAG.
# - Query rewriting.
# - Retrieval evaluation.
# - Source citations.

# Install:pip install pypdf faiss-cpu sentence-transformers langchain-community


### Code 22: Load a PDF

# Create `09_rag_agents/01_pdf_loader.py`.

from pypdf import PdfReader

reader = PdfReader(
    r"C:\Users\DELL\Desktop\Agentic_AI_Complete_Course\09_rag_agents\sample.pdf"
)
text = ""
for page in reader.pages:
    text += page.extract_text() or ""
    print(text)

# Place a PDF called `sample.pdf` inside the same folder.
