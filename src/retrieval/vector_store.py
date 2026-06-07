from langchain_community.vectorstores import FAISS
import os


def create_or_load_vectorstore(chunks, embedding_model):

    faiss_path = "vectorstore/faiss_index"

    if os.path.exists(
        os.path.join(faiss_path, "index.faiss")
    ):

        print("Loading Existing FAISS Index...")

        vectorstore = FAISS.load_local(
            faiss_path,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        return vectorstore

    print("Creating New FAISS Index...")

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vectorstore.save_local(
        faiss_path
    )

    print("FAISS Index Saved")

    return vectorstore