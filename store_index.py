from dotenv import load_dotenv
import os
from src.helper import load_pdf, filter_to_minimal_docs, text_splitter
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

book_path = "./data/book2.pdf"

extracted_data = load_pdf(book_path)
filtered_data = filter_to_minimal_docs(extracted_data)
splitted_data = text_splitter(filtered_data)

pc = Pinecone(api_key=PINECONE_API_KEY)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

index_name = "medical-book-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec = ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

pinecone_store = PineconeVectorStore.from_documents(
    documents = splitted_data,
    index_name = index_name,
    embedding = embedding_model
)