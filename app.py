import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
import random
import time

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamed response emulator
def response_generator():
    response = st.session_state.ai_response
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    #分割資料：語言模型受到它們可以處理的資料長度（稱為上下文長度）的限制
    #執行 RAG 的文字可能會很大。搜尋大塊資料也可能很困難
    #文字分成多個稱為區塊的小塊，以使檢索和產生更快更容易
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    #嵌入是文字的向量表示。將文字轉換為某種向量使我們能夠對其應用數學運算
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.session_state.ai_response = response["output_text"]
    #st.write("Reply: ", st.session_state.ai_response)

def main():
    st.set_page_config("License Assistant", page_icon=":scroll:")
    st.header("Help Certificate - Chat with AI ")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_question = st.text_input(
        "Inside the investigation, investigation and investigation...")

    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)
        user_input(user_question)
        st.session_state.messages.append({"role": "assistant", "content": st.session_state.ai_response})
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())

    with st.sidebar:
        st.title("Select the PDF file to upload!")
        pdf_docs = st.file_uploader(
            "Upload PDF Files then \n Click on the Submit ", accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px; text-align: center;">
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
