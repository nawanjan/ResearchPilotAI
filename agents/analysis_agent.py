from models.groq_client import client


def analysis_agent(results):
    """
    Analysis Agent
    Uses Groq AI to summarize retrieved research papers.
    """

    context = ""

    for result in results:
        context += result.page_content + "\n\n"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert research assistant. "
                    "Read the retrieved research papers and produce a clear, concise academic summary."
                )
            },
            {
                "role": "user",
                "content": context
            }
        ]
    )

    return response.choices[0].message.content