from langchain_community.document_loaders import PyPDFDirectoryLoader
import os

def load_documents():
    # PDF folder path
    pdf_folder = os.path.join("knowledge_base", "papers")

    # Load all PDF files
    loader = PyPDFDirectoryLoader(pdf_folder)
    documents = loader.load()

    return documents