import streamlit as st
import os
from styles import load_css

from rag.loader import load_documents
from rag.chunker import split_documents
from rag.retriever import create_vector_store

from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.reflection_agent import reflection_agent


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ResearchPilot AI",
    page_icon="🤖",
    layout="wide"
)
st.markdown(load_css(), unsafe_allow_html=True)
def get_pdf_count():

    pdf_folder = "knowledge_base/papers"

    if not os.path.exists(pdf_folder):
        return 0

    pdf_files = [
        file
        for file in os.listdir(pdf_folder)
        if file.lower().endswith(".pdf")
    ]

    return len(pdf_files)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 ResearchPilot AI")

    st.markdown("---")

    st.subheader("📌 System Information")

    st.write("🤖 AI Model : Llama 3.1 8B Instant")
    st.write("📂 Vector Database : ChromaDB")
    st.write("📄 Knowledge Base : Research Papers")
    st.write("🔍 Retrieval Method : RAG")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("Nawanjan Rupasinghe")

    st.markdown("---")

    st.success("System Ready ✅")


# -----------------------------
# Title
# -----------------------------
st.title("🤖 ResearchPilot AI")

st.markdown("""
Analyze research papers using **Retrieval-Augmented Generation (RAG)** and **Multi-Agent AI**.

Enter your research question below and click **Analyze**.
""")
# -----------------------------
# Dashboard Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
   st.metric("📄 Research Papers", get_pdf_count())

with col2:
    st.metric("🤖 AI Model", "Llama 3.1")

with col3:
    st.metric("🗂️ Vector DB", "ChromaDB")



# -----------------------------
# Load Knowledge Base
# -----------------------------
@st.cache_resource
def load_knowledge_base():
    documents = load_documents()
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)
    return vector_store


with st.spinner("Loading Knowledge Base..."):
    vector_store = load_knowledge_base()

st.success("Knowledge Base Loaded Successfully!")

st.divider()

# -----------------------------
# User Input
# -----------------------------
st.subheader("📝 Ask a Research Question")

question = st.text_input(
    "Enter your research question:"
)

analyze_button = st.button(
    "🚀 Analyze",
    use_container_width=True
)

# -----------------------------
# AI Workflow
# -----------------------------
if analyze_button:

    if question.strip() == "":
        st.warning("Please enter a research question.")

    else:

        with st.spinner("Searching Research Papers..."):
            results = research_agent(vector_store, question)

        with st.spinner("Generating AI Summary..."):
            summary = analysis_agent(results)

        with st.spinner("Reviewing Final Answer..."):
            final_answer = reflection_agent(summary)

        st.success("Analysis Completed Successfully!")

        st.divider()

        st.subheader("📄 Retrieved Research Papers")

        for i, result in enumerate(results, start=1):
            with st.expander(f"Research Paper {i}"):
                st.write(result.page_content)

        st.divider()

        st.subheader("🤖 AI Summary")
        st.info(summary)

        st.divider()

        st.subheader("✅ Final Reviewed Answer")
        st.success(final_answer)

        st.divider()

        st.download_button(
            label="📥 Download Final Answer",
            data=final_answer,
            file_name="ResearchPilotAI_Result.txt",
            mime="text/plain"
        )