# RAG From Scratch

Learning Retrieval-Augmented Generation (RAG) and FastAPI from scratch.

---

## Roadmap

✅ Phase 0: Environment Setup

✅ Phase 1: Document Loading

✅ Phase 2: Chunking

✅ Phase 3: Embeddings

✅ Phase 4: Vector Database

✅ Phase 5: Retrieval

✅ Phase 6: Prompt Construction

✅ Phase 7: Generation

✅ Phase 8: Production Improvements

✅ Phase 9: FastAPI Integration

---

# What I've Learned

## Phase 1 - Document Loading

- Used PyPDFLoader to load PDF documents
- Learned about LangChain Document objects
- Explored page_content and metadata
- Successfully loaded multi-page PDFs

---

## Phase 2 - Chunking

- Used RecursiveCharacterTextSplitter
- Learned chunk_size and chunk_overlap
- Split documents into smaller searchable chunks
- Understood why chunking improves retrieval quality
- Learned how metadata is preserved during chunking

---

## Phase 3 - Embeddings

- Used Sentence Transformers (`all-MiniLM-L6-v2`)
- Generated vector embeddings from text
- Learned semantic similarity concepts
- Compared embeddings using cosine similarity
- Understood how text becomes numerical vectors
- Learned why embeddings are required before retrieval

---

## Phase 4 - Vector Database

- Used FAISS as a vector database
- Stored document embeddings efficiently
- Created a searchable vector store
- Connected chunks with embeddings and metadata
- Learned how vector databases differ from traditional databases

---

## Phase 5 - Retrieval

- Implemented similarity search using FAISS
- Converted user questions into embeddings
- Retrieved the most relevant document chunks
- Learned the role of the `k` parameter
- Understood retrieval relevance and ranking

---

## Phase 6 - Prompt Construction

- Built prompts dynamically using retrieved context
- Combined context and user questions
- Learned grounding techniques in RAG
- Understood how prompt design affects answer quality

---

## Phase 7 - Generation

- Integrated Groq API
- Used Llama 3.3 70B Versatile model
- Sent retrieved context to an LLM
- Generated answers from PDF content
- Built a complete end-to-end RAG pipeline

---

## Phase 8 - Production Improvements

### Modular Project Structure

Refactored the project into a production-style architecture:

- loaders
- chunking
- embeddings
- retrieval
- prompts
- llm
- rag

### FAISS Persistence

- Saved vector database locally
- Loaded existing indexes automatically
- Eliminated unnecessary re-embedding
- Reduced startup time

### Source Citations

- Returned source document information
- Displayed page references
- Improved answer transparency
- Learned how production RAG systems provide traceability

---

## Phase 9 - FastAPI Integration

### Built REST API Endpoints

Created:

- GET `/`
- POST `/ask`

### Request Validation

Used Pydantic models:

```python
class QuestionRequest(BaseModel):
    question: str
```

### Swagger Documentation

Used FastAPI's built-in:

```text
/docs
```

interactive API testing interface.

### RAG API Service

Connected:

```text
FastAPI
↓
RAG Pipeline
↓
FAISS Retrieval
↓
Groq LLM
↓
JSON Response
```

### Example Request

```json
{
    "question": "What is the salary?"
}
```

### Example Response

```json
{
    "answer": "The salary is Rs 21,700/- + allowances..."
}
```

---

# Final Project Structure

```text
RAG-Learning/
│
├── data/
│   └── sample.pdf
│
├── learning/
│   ├── phase1_2_loading_chunking.py
│   ├── phase3_embeddings.py
│   ├── phase4_5_vector_db_retrieval.py
│   ├── phase6_prompt_construction.py
│   └── phase7_generation.py
│
├── src/
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── loaders/
│   │   ├── __init__.py
│   │   └── pdf_loader.py
│   │
│   ├── chunking/
│   │   ├── __init__.py
│   │   └── text_splitter.py
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── embedding_model.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── prompt_builder.py
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   └── groq_client.py
│   │
│   └── rag/
│       ├── __init__.py
│       └── pipeline.py
│
├── vectorstore/
│   └── faiss_index/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---

# Final Architecture

```text
PDF
↓
Document Loader
↓
Chunking
↓
Embeddings
↓
FAISS Vector Database
↓
Similarity Retrieval
↓
Prompt Construction
↓
Groq (Llama 3.3 70B)
↓
Generated Answer
↓
FastAPI Endpoint
↓
JSON Response
```

---

# Key Technologies Used

- Python
- LangChain
- Sentence Transformers
- FAISS
- Groq API
- Llama 3.3 70B
- FastAPI
- Pydantic
- Uvicorn

---

# Running the Project

## Start FastAPI Server

```bash
uvicorn src.api.main:app --reload
```

---

## Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Ask Questions

Example:

```json
{
    "question": "What is the salary?"
}
```

---

# Learning Outcome

This project helped me understand the complete RAG pipeline from scratch:

- Document Loading
- Chunking
- Embeddings
- Vector Databases
- Retrieval
- Prompt Engineering
- LLM Generation
- FastAPI APIs
- Production-Oriented Project Structure

The result is a fully functional RAG API capable of answering questions from PDF documents using semantic search and a Large Language Model.