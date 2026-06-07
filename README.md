# RAG From Scratch

Learning Retrieval-Augmented Generation (RAG) and FastAPI from scratch.

## Roadmap

✅ Phase 0: Environment Setup

✅ Phase 1: Document Loading

✅ Phase 2: Chunking

✅ Phase 3: Embeddings

✅ Phase 4: Vector Databases

✅ Phase 5: Retrieval

✅ Phase 6: Prompt Construction

✅ Phase 7: Generation

✅ Phase 8: Production Improvements

⬜ Phase 9: FastAPI

## What I've Learned So Far

### Phase 1 - Document Loading

* Used PyPDFLoader to load PDFs
* Learned LangChain Document objects
* Explored page_content and metadata
* Loaded a 7-page PDF successfully

### Phase 2 - Chunking

* Used RecursiveCharacterTextSplitter
* Learned chunk_size and chunk_overlap
* Split 7 documents into 48 chunks
* Understood why chunking improves retrieval
* Learned how metadata is preserved after chunking

### Phase 3 - Embeddings

* Used Sentence Transformers (`all-MiniLM-L6-v2`)
* Generated vector embeddings from text
* Learned how semantic similarity works
* Used cosine similarity to compare embeddings
* Verified that similar meanings produce higher similarity scores
* Understood how text is converted into 384-dimensional vectors
* Learned why embeddings are required before retrieval

### Phase 4 - Vector Database

* Used FAISS as a vector database
* Stored embeddings efficiently for similarity search
* Learned how vector databases differ from traditional databases
* Connected document chunks with their embeddings and metadata
* Created a searchable vector store from PDF content

### Phase 5 - Retrieval

* Implemented similarity search using FAISS
* Converted user questions into embeddings
* Retrieved the most relevant chunks from the vector database
* Learned the importance of the `k` parameter in retrieval
* Understood the trade-off between retrieval quantity and relevance

### Phase 6 - Prompt Construction

* Built prompts dynamically using retrieved context
* Combined context and user query into a structured prompt
* Learned how RAG systems ground LLM responses using retrieved information
* Understood why prompt design affects answer quality

### Phase 7 - Generation

* Integrated Groq API with Llama 3.3 70B
* Sent retrieved context to an LLM
* Generated answers based on document content
* Built a complete end-to-end RAG pipeline
* Implemented interactive question answering from PDFs

### Phase 8 - Production Improvements

* Refactored the project into a modular architecture
* Separated responsibilities into loaders, chunking, embeddings, retrieval, prompts, llm, and rag modules
* Added persistent FAISS storage using `save_local()`
* Loaded existing FAISS indexes using `load_local()`
* Eliminated unnecessary re-embedding on every run
* Added source citations using document metadata
* Displayed source PDF and page numbers for retrieved answers
* Learned how production RAG systems reuse vector databases
* Improved maintainability through structured project organization

## Project Structure

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
│   ├── loaders/
│   ├── chunking/
│   ├── embeddings/
│   ├── retrieval/
│   ├── prompts/
│   ├── llm/
│   └── rag/
│
├── vectorstore/
│   └── faiss_index/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

The `learning` folder contains the phase-by-phase implementations created while learning RAG concepts.

The `src` folder contains the modular production-style implementation of the complete RAG pipeline.

## Current Pipeline

```text
PDF
↓
Document Loader
↓
Document Objects
↓
Chunking
↓
Chunk Documents
↓
Embeddings
↓
FAISS Vector Database
↓
Similarity Retrieval
↓
Prompt Construction
↓
Groq LLM (Llama 3.3 70B)
↓
Generated Answer
↓
Source Citations
```

## Example Output

```text
Question:
What is the salary?

Generated Answer:
The salary is Rs 21,700/- + allowances (Level-3, Cell-1)
as per the new pay matrix of the 7th CPC.

Source Information:
--------------------
File: data/sample.pdf
Page: 1
```

## Next Step

```text
Current RAG Pipeline
↓
FastAPI Backend
↓
REST API Endpoints
↓
RAG API Service
```