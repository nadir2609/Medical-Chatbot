# 🏥 AI Medical Assistant Chatbot

A RAG-based (Retrieval-Augmented Generation) medical chatbot built with Flask, LangChain, Pinecone, and OpenAI. It answers medical questions using context retrieved from PDF documents.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)

## Features

- **RAG Pipeline** — Retrieves relevant context from medical PDFs stored in Pinecone vector database
- **LLM-Powered Responses** — Uses OpenAI-compatible models via OpenRouter for concise, accurate answers
- **Modern Chat UI** — Clean, responsive interface with typing indicators and message animations
- **PDF Ingestion** — Processes and indexes PDF documents for knowledge retrieval

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Flask |
| LLM Framework | LangChain |
| Vector Store | Pinecone |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| LLM | OpenAI via OpenRouter |
| Frontend | HTML, CSS, JavaScript |

## Project Structure

```
AI Chatbot/
├── app.py                 # Flask application & RAG chain
├── store_index.py         # PDF ingestion & Pinecone indexing
├── requirements.txt       # Python dependencies
├── setup.py               # Package setup
├── src/
│   ├── __init__.py
│   ├── helper.py          # PDF loading & text splitting utilities
│   └── prompt.py          # System prompt template
├── static/
│   └── style.css          # Chat UI styles
├── templates/
│   └── index.html         # Chat UI template
├── data/                  # PDF documents (not tracked)
└── notebooks/             # Jupyter notebooks (not tracked)
```

## Getting Started

### Prerequisites

- Python 3.12+
- [Pinecone](https://www.pinecone.io/) account & API key
- [OpenRouter](https://openrouter.ai/) API key (or OpenAI API key)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ai-medical-chatbot.git
   cd ai-medical-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate        # Linux/Mac
   env\Scripts\Activate.ps1       # Windows PowerShell
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openrouter_api_key
   ```

5. **Index your PDF documents**

   Place your medical PDF in the `data/` folder, then run:
   ```bash
   python store_index.py
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open in browser**

   Navigate to `http://localhost:8000`

## How It Works

1. **Document Ingestion** — `store_index.py` loads a PDF, splits it into chunks, generates embeddings using HuggingFace, and stores them in Pinecone.
2. **Query Processing** — When a user sends a question, the retriever fetches the top 3 most relevant chunks from Pinecone.
3. **Response Generation** — The retrieved context and question are passed to the LLM, which generates a concise medical answer (max 3 sentences).

## License

This project is open source and available under the [MIT License](LICENSE).
