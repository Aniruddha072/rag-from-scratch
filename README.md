# RAG From Scratch

Learning Retrieval-Augmented Generation (RAG) and FastAPI from scratch.

## Roadmap

✅ Phase 0: Environment Setup

✅ Phase 1: Document Loading

✅ Phase 2: Chunking

✅ Phase 3: Embeddings

✅ Phase 4: Vector Databases

✅ Phase 5: Retrieval

⬜ Phase 6: Prompt Construction

⬜ Phase 7: Generation

⬜ Phase 8: Complete RAG

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

### Phase 4 - Vector Databases

* Installed and used FAISS as a local vector database
* Stored chunk embeddings inside a searchable vector index
* Learned how vector databases optimize similarity search
* Understood how embeddings, chunk text, and metadata are linked together

### Phase 5 - Retrieval

* Performed semantic search using FAISS
* Retrieved the top-k most relevant chunks for a query
* Tested retrieval with age limit, salary, and qualification queries
* Learned the impact of the k parameter on retrieval quality
* Observed how chunk size and embeddings affect search results
* Understood the complete retrieval flow in a RAG system

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
Retrieval
```

## Next Step

```text
Retrieved Chunks
↓
Prompt Construction
↓
LLM
↓
Generated Answer
```
