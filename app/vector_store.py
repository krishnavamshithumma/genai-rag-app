from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import OPENAI_API_KEY

def create_vectorstore(docs):
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    return FAISS.from_documents(docs, embeddings)
