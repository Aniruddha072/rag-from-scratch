from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

#Load PDF

loader = PyPDFLoader("sample.pdf")
documents = loader.load()

#Chunk Documents

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

#Load Embedding Model

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#Create Vector Store

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

#Query
query = "What is the salary?"

#Retrieve Relevant Chunks
results = vectorstore.similarity_search(
    query,
    k=3
)

#Combine Retrieved Chunks
context = "\n\n".join(
    [doc.page_content for doc in results]
)

#Build Prompt

prompt = f"""
You are a helpful assistant.

Answer the question only using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

print(prompt)