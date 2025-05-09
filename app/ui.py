import streamlit as st
from tempfile import NamedTemporaryFile
from app.loader import load_pdf
from app.vector_store import create_vectorstore
from app.qa_chain import create_chain

def run_app():
    st.set_page_config(page_title="PDF Q&A", layout="wide")
    st.title("📄 Intelligent Manual Assistant")

    uploaded_file = st.file_uploader("Upload your PDF manual", type=["pdf"])

    if uploaded_file:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        docs = load_pdf(pdf_path)
        vectorstore = create_vectorstore(docs)
        qa_chain, memory = create_chain(vectorstore)

        st.subheader("Ask a question:")
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        query = st.text_input("Your question")
        if query:
            result = qa_chain.invoke({"question": query})
            st.session_state.chat_history.append((query, result["answer"]))

        if st.session_state.chat_history:
            st.markdown("### Chat History")
            for q, a in st.session_state.chat_history:
                st.markdown(f"**You:** {q}")
                st.markdown(f"**Assistant:** {a}")
