import streamlit as st
from functions import (
    get_pdf_text, get_text_chunks, get_vectorstore, get_conversation_chain,
    get_text_chunks_from_docx, get_vectorstore_from_docx, get_conversation_chain_for_docx,
    get_text_chunks_from_ppt, get_vectorstore_from_ppt, get_conversation_chain_for_ppt,
    get_text_chunks_from_excel, get_vectorstore_from_excel, get_conversation_chain_for_excel
)
import os

def handle_userinput(user_question):
    if 'conversation' in st.session_state:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history.append((user_question, response['answer']))
        st.write(response['answer'])

def main():
    st.set_page_config(page_title="AI Chat with Documents 📚", layout="wide", page_icon=":books:")
    st.sidebar.header("Configuration")
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    else:
        st.error("Please enter your OpenAI API key.")

    st.title("AI Chat with Documents 📚")
    st.write("Upload a document (PDF, Word, PowerPoint, Excel) and start chatting with it!")
    uploaded_files = st.file_uploader("Upload a document", type=["pdf", "docx", "pptx", "xlsx"], accept_multiple_files=True)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if uploaded_files:
        for uploaded_file in uploaded_files:
            raw_text = ""
            if uploaded_file.name.endswith('.pdf'):
                raw_text += get_pdf_text([uploaded_file])
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
            elif uploaded_file.name.endswith('.docx'):
                text_chunks = get_text_chunks_from_docx(uploaded_file)
                vectorstore = get_vectorstore_from_docx(text_chunks)
                st.session_state.conversation = get_conversation_chain_for_docx(vectorstore)
            elif uploaded_file.name.endswith('.pptx'):
                text_chunks = get_text_chunks_from_ppt(uploaded_file)
                vectorstore = get_vectorstore_from_ppt(text_chunks)
                st.session_state.conversation = get_conversation_chain_for_ppt(vectorstore)
            elif uploaded_file.name.endswith('.xlsx'):
                text_chunks = get_text_chunks_from_excel(uploaded_file)
                vectorstore = get_vectorstore_from_excel(text_chunks)
                st.session_state.conversation = get_conversation_chain_for_excel(vectorstore)

            st.success(f"Document {uploaded_file.name} processed successfully! Ask your questions below.")

    user_question = st.text_input("Ask a question about the document:")
    if st.button("Submit") and user_question and 'conversation' in st.session_state:
        handle_userinput(user_question)

    if st.session_state.chat_history:
        st.write("### Chat History")
        for i, (question, answer) in enumerate(st.session_state.chat_history):
            st.write(f"**Q: {question}**")
            st.write(f"**A: {answer}**")

    if st.button("Clear Chat"):
        st.session_state.chat_history = []

    st.markdown("---")
    st.markdown("👤 **Created by [Anish Mahapatra](https://www.linkedin.com/in/anishmahapatra/)**")

if __name__ == "__main__":
    main()