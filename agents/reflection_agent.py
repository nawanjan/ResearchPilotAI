from models.groq_client import client


def reflection_agent(summary):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content":
                "You are a senior research reviewer. Improve the given academic summary. Make it clearer, more structured and professional."
            },
            {
                "role": "user",
                "content": summary
            }
        ]
    )

    return response.choices[0].message.content