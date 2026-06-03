# RAG From Scratch

Learning Retrieval-Augmented Generation (RAG) and FastAPI from scratch.

## Roadmap

✅ Phase 0: Environment Setup

✅ Phase 1: Document Loading

✅ Phase 2: Chunking

✅ Phase 3: Embeddings

⬜ Phase 4: Vector Databases

⬜ Phase 5: Retrieval

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
```

## Next Step

```text
Embeddings
↓
Vector Database
```
