from rag.loader import load_documents
from rag.chunker import split_documents
from rag.retriever import create_vector_store, search_documents
from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from models.groq_client import client
# Load documents
documents = load_documents()
print(f"Total Documents Loaded: {len(documents)}")

# Split documents into chunks
chunks = split_documents(documents)
print(f"Total Chunks Created: {len(chunks)}")

# Create vector database
vector_store = create_vector_store(chunks)
print("✅ Vector Database Ready!")

# Search Query
query = "What are the main causes of in-flight emergencies?"

results = research_agent(vector_store, query)

print("\n========== SEARCH RESULTS ==========\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}")
    print("-" * 50)
    print(result.page_content[:500])
    print()

    summary = analysis_agent(results)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(summary)
print("\n" + "=" * 60)
print("TESTING GROQ")
print("=" * 60)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Say Hello from Groq AI."
        }
    ]
)

print(response.choices[0].message.content)