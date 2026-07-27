from rag.retriever import search_documents


def research_agent(vector_store, question):
    """
    Research Agent
    Finds the most relevant document chunks.
    """

    results = search_documents(vector_store, question)

    return results