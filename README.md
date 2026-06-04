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

⬜ Phase 8: RAG Improvements

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

* Used FAISS as a local vector database
* Stored chunk embeddings in a searchable vector index
* Learned how vector databases enable efficient similarity search
* Understood how embeddings, chunk text, and metadata are stored together

### Phase 5 - Retrieval

* Performed semantic search using FAISS
* Retrieved the top-k most relevant chunks for a query
* Tested retrieval using salary, age limit, qualifications, and application-related questions
* Learned the impact of the k parameter on retrieval quality
* Observed how chunk size affects retrieval performance
* Understood the complete retrieval workflow in a RAG system

### Phase 6 - Prompt Construction

* Combined retrieved chunks into a single context block
* Learned how to construct prompts dynamically using f-strings
* Added instructions, context, and user questions into a structured prompt
* Understood how retrieved information augments the LLM prompt
* Learned that prompts are ultimately just formatted strings sent to an LLM

### Phase 7 - Generation

* Integrated Groq API with Llama 3.3 70B
* Sent retrieved context and user queries to an LLM
* Generated answers using retrieved document information
* Built an interactive question-answering system using terminal input
* Added source page tracking for retrieved answers
* Completed a full end-to-end RAG pipeline

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
↓
Prompt Construction
↓
Groq Llama 3.3 70B
↓
Generated Answer
```

## Example Query

```text
Question:
How to submit application?

Answer:
Candidates are requested to submit the application form through their registered email to:
sunshine.rise@nic.in
```

## Next Step

```text
Complete RAG Pipeline
↓
Improve Retrieval Quality
↓
Source Citations
↓
Multiple Documents
↓
FastAPI Integration
```
