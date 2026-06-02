# RAG From Scratch

Learning Retrieval-Augmented Generation (RAG) and FastAPI from scratch.

## Roadmap

✅ Phase 0: Environment Setup

✅ Phase 1: Document Loading

✅ Phase 2: Chunking

⬜ Phase 3: Embeddings

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
```

## Next Step

```text
Chunk Documents
↓
Embeddings
```
