from dotenv import load_dotenv
import os

from groq import Groq

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

#Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

#Chunk Documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

#Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#Vector Database
vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

#User Question
query = input("Enter your question: ")

#Retrieval
results = vectorstore.similarity_search(
    query,
    k=1
)

print("\nSource Page:")
print(results[0].metadata["page"] + 1)

#Build Context
context = "\n\n".join(
    [doc.page_content for doc in results]
)

#Prompt Construction
prompt = f"""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer exists in the context, give a direct answer in one sentence.

Context:
{context}

Question:
{query}

Answer:
"""

#Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

#Generation

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

#Answer
print("\nQuestion:")
print(query)

print("\nGenerated Answer:")
print(response.choices[0].message.content)