
# 📘 Chat with Multiple PDFs (RAG App)

A Streamlit-based AI-powered app that allows you to upload multiple PDFs and chat with them using Retrieval-Augmented Generation (RAG). It uses vector embeddings (FAISS + Hugging Face), chunked text retrieval, and a conversational memory chain to answer questions based only on your uploaded documents.


## 🚀 Features

- 📄 Upload multiple PDFs and clear old files automatically
- ✂️ Chunk long documents for retrieval
- 🔍 Store and search chunks using FAISS
- 🧠 Query-relevant chunks + memory via LangChain’s `ConversationalRetrievalChain`
- 🤖 Powered by `google/flan-t5-xxl` on Hugging Face (free, no OpenAI needed)
- 💬 Beautiful chat UI with user/bot avatars and memory

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: `google/flan-t5-xxl` via Hugging Face Hub
- **Embeddings**: `BAAI/bge-base-en-v1.5`
- **Vector Store**: FAISS
- **Text Extraction**: PyMuPDF (via `PyPDFLoader`)
- **RAG Framework**: LangChain

## 📁 Folder Structure

```
chatapp/
│
├── app.py
├── requirements.txt
├── .env               
├── data/              # PDF uploads
├── src/
│   ├── loader.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── template.py
```

## ⚙️ Installation

```bash
git clone https://github.com/thesunil-sah/Chatapp
cd chatapp
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file with:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
OPENAI_API_KEY=your_api_key
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 📦 Requirements

Make sure `requirements.txt` includes:

```
streamlit
langchain
langchain-community
faiss-cpu
sentence-transformers
huggingface-hub
python-dotenv
PyMuPDF
```

## 🤝 Credits

- Built using [LangChain](https://github.com/hwchase17/langchain)
- Hugging Face model: `google/flan-t5-xxl`
- Inspired by the RAG concept
