import streamlit as st
import tempfile
import os

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline

from transformers import pipeline

# ------------------ UI ------------------
st.set_page_config(page_title="RAG Document Q&A", layout="centered")
st.title("AI Document Question Answering (RAG)")
st.write("Upload a PDF and ask questions — **No Internet / No API Key required**")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# ------------------ Load LLM ------------------
@st.cache_resource
def load_llm():
    pipe = pipeline(
        task="text2text-generation",   # ✅ CORRECT TASK
        model="google/flan-t5-small",   # ✅ INSTRUCTION MODEL
        max_new_tokens=128
    )
    return HuggingFacePipeline(pipeline=pipe)

llm = load_llm()

# ------------------ Main Logic ------------------
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    question = st.text_input("Ask a question from the document")

    if st.button("Get Answer") and question.strip():
        docs = retriever.get_relevant_documents(question)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
Answer ONLY using the context below.
If the answer is not present, reply exactly:
Not found in document.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = llm(prompt)

        st.subheader("Answer")
        st.write(answer.strip())

    os.remove(pdf_path)