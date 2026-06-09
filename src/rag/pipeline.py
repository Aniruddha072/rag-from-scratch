from src.loaders.pdf_loader import load_pdf
from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model
from src.retrieval.vector_store import create_or_load_vectorstore
from src.retrieval.retriever import retrieve_documents
from src.prompts.prompt_builder import build_prompt
from src.llm.groq_client import ask_groq


def run_pipeline(query):

    docs = load_pdf("data/sample.pdf")

    chunks = split_documents(docs)

    embedding_model = get_embedding_model()

    vectorstore = create_or_load_vectorstore(
        chunks,
        embedding_model
    )


    results = retrieve_documents(
        vectorstore,
        query
    )

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    prompt = build_prompt(
        context,
        query
    )

    answer = ask_groq(prompt)

    print("\nQuestion:")
    print(query)

    print("\nGenerated Answer:")
    print(answer)

    print("\nSource Information:")
    print("-" * 20)

    seen = set()

    for doc in results:

        source = (
            doc.metadata.get("source"),
            doc.metadata.get("page")
        )

        if source in seen:
            continue

        seen.add(source)

        print(
            f"File: {doc.metadata.get('source')}"
        )

        print(
            f"Page: {doc.metadata.get('page') + 1}"
        )

        print()

    return answer