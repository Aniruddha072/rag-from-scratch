def build_prompt(context, query):

    return f"""
You are a helpful assistant.

Answer only using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""