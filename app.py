from flask import Flask, render_template, jsonify, request
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.prompt import system_prompt
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

app = Flask(__name__)


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

index_name = "medical-book-index"

pinecone_store = PineconeVectorStore.from_existing_index(
    index_name=index_name, embedding=embedding_model
)

retriever = pinecone_store.as_retriever(search_kwargs={"k": 3})

model = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="openai/gpt-oss-120b",
)

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "{question}")]
)

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chat():
    msg = request.get_json().get("message")
    response = rag_chain.invoke(msg)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
