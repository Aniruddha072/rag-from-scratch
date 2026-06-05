from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks, embedding_model):

    return FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )