from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("sample.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

chunks = splitter.split_documents(docs)

print("Original Documents:", len(docs))
print("Chunks Created:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nSecond Chunk:\n")
print(chunks[1].page_content)

print("\nChunk 0 Length:", len(chunks[0].page_content))
print("Chunk 1 Length:", len(chunks[1].page_content))

print("\nChunk Metadata:")
print(chunks[0].metadata)
