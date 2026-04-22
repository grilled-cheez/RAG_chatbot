# RAG Chatbot

A Retrieval Augmented Generation (RAG) chatbot built with Streamlit that allows you to upload PDF documents and ask questions about their content. The chatbot retrieves relevant information from your documents and generates accurate answers using the Llama3 LLM.

## Features

- 📄 **PDF Upload & Processing**: Upload multiple PDF files and automatically process them into a vector database
- 🔍 **Semantic Search**: Find relevant document chunks based on your queries using embeddings
- 💬 **Interactive Chat**: Ask questions about your documents and get AI-powered responses
- 💾 **Chat History**: Download conversation logs for future reference
- 🧪 **ChromaDB Inspector**: Test queries directly against your vector store to inspect retrieved chunks
- 🚀 **Fast Responses**: Powered by Groq API with Llama3 8B model for quick inference

## Prerequisites

- Python 3.13 or higher
- A Groq API key (get it [here](https://console.groq.com/keys))

## Installation

1. **Clone or download the repository**:
   ```bash
   cd RAG_chatbot
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or using uv (if installed):
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run index.py
   ```

2. **The app will open in your browser** at `http://localhost:8501`

3. **Upload PDF files**:
   - Click "Choose files" in the sidebar to select one or more PDF documents
   - Click "Submit to DB" to process and add them to the vector store

4. **Ask questions**:
   - Type your questions in the chat input box
   - The chatbot will search relevant chunks from your PDFs and generate answers

5. **Inspect vector store** (optional):
   - Use the "🔍 Test a query against ChromaDB" search box in the sidebar
   - View the top 3 matching document chunks for any query

6. **Download chat history**:
   - After chatting, click the "💾 Download Chat History" button to save your conversation

## Project Structure

```
RAG_chatbot/
├── index.py                    # Main Streamlit application
├── requirements.txt            # Python package dependencies
├── pyproject.toml             # Project configuration
├── README.md                  # This file
├── chroma_store/              # Vector database storage (created on first use)
│   ├── chroma.sqlite3
│   └── [embedding_data]/
└── modules/
    ├── chat.py                # Chat history and UI functions
    ├── llm.py                 # LLM chain setup (Groq + Llama3)
    ├── pdfhandler.py          # PDF file upload and saving
    ├── vectorstore.py         # Vector store initialization and document loading
    └── chroma_inspector.py    # ChromaDB inspection tools
```

## How It Works

1. **PDF Processing**: PDFs are loaded using `PyPDFLoader` and split into chunks (1000 characters with 200 overlap) using `RecursiveCharacterTextSplitter`

2. **Embeddings**: Text chunks are converted to embeddings using HuggingFace's `all-MiniLM-L12-v2` model

3. **Vector Store**: Embeddings are stored in ChromaDB for efficient similarity search

4. **Retrieval**: When you ask a question, the system finds the 3 most relevant document chunks using semantic similarity

5. **Generation**: The retrieved chunks and your question are sent to Groq's Llama3 8B model to generate a contextual response

## Configuration

### Embedding Model
- Currently using: `all-MiniLM-L12-v2` (fast, 384-dimensional embeddings)
- Located in: [modules/vectorstore.py](modules/vectorstore.py)

### LLM Model
- Currently using: `llama3-8b-8192` via Groq API
- Located in: [modules/llm.py](modules/llm.py)

### Vector Store
- Database: ChromaDB
- Persistence: `./chroma_store/`
- Located in: [modules/vectorstore.py](modules/vectorstore.py)

## Troubleshooting

**Issue**: "GROQ_API_KEY not found"
- Make sure you've created a `.env` file with your API key

**Issue**: "Could not fetch document count" in ChromaDB Inspector
- Ensure you've uploaded and submitted PDFs first

**Issue**: Slow responses
- This depends on your internet connection and Groq API availability
- Try with smaller PDFs or fewer documents initially

**Issue**: Out of memory
- Reduce the number of PDF pages or chunk size in [modules/vectorstore.py](modules/vectorstore.py)

## Dependencies

- **streamlit**: Web UI framework
- **langchain-groq**: LLM integration with Groq
- **langchain-community**: RAG pipeline components
- **pypdf**: PDF parsing
- **sentence-transformers**: Embedding generation
- **chromadb**: Vector database
- **python-dotenv**: Environment variable management
- **transformers**: NLP utilities

## Future Improvements

- Support for additional document formats (DOCX, TXT, etc.)
- Custom embedding model selection
- Multiple LLM provider options
- Query history and analytics
- Adjustable RAG parameters (chunk size, overlap, retrieval count)
- User authentication and document permissions

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
