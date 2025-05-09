from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
from langchain.chains import ConversationalRetrievalChain
from app.config import OPENAI_API_KEY

def create_chain(vectorstore):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer")
    retriever = vectorstore.as_retriever()
    return ConversationalRetrievalChain.from_llm(
        llm=OpenAI(temperature=0, api_key=OPENAI_API_KEY),
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer"
    ), memory
