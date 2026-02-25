from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

def filter_to_minimal_docs(documents: List[Document]) -> List[Document]:
    minimal_docs = []
    for doc in documents:
        minimal_doc = Document(
            page_content=doc.page_content,
            metadata={"source": doc.metadata.get("source", "unknown")}
        )
        minimal_docs.append(minimal_doc)
    return minimal_docs

def text_splitter(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=20)
    chunks = text_splitter.split_documents(documents)
    return chunks
