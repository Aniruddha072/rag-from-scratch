def retrieve_documents(vectorstore, query):

    return vectorstore.similarity_search(
        query,
        k=1
    )