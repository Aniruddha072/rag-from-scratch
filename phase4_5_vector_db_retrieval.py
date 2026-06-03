from langchain_community import document_loaders
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

#Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("Documents Loaded:", len(documents))

#Chunk Documents

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)
chunks = splitter.split_documents(documents)

print("Chunks Created:", len(chunks))

#Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("Embedding Model Loaded")

#FAISS Vector Store
vectorstore = FAISS.from_documents(
    documents = chunks,
    embedding = embedding_model
) 

print("FAISS Vector Database Created")

print("\nFirst Chunk:")
print(chunks[0].page_content[:200])

print("\nMetadata:")
print(chunks[0].metadata)

print("\n\n========================")
print("SIMILARITY SEARCH")
print("========================")

query = "What are the qualifications?"

results = vectorstore.similarity_search(query, k=3)

print(f"\nQuery: {query}")

print("\nTop 3 Retrieved Chunks:\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}")
    print("-" * 50)
    print(doc.page_content[:300])
    print("\nPage:", doc.metadata["page"] + 1)
    print()