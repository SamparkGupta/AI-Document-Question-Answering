📄 AI Document Question Answering System (RAG)

An AI-powered application that allows users to upload PDF documents and ask natural language questions to retrieve relevant information. The system uses Retrieval-Augmented Generation (RAG) to ensure answers are grounded in document content instead of relying solely on the language model’s knowledge.

This project demonstrates how Large Language Models (LLMs), vector databases, and semantic search can be combined to build an intelligent document analysis system.

🚀 Key Features

✔ Upload and analyze PDF documents
✔ Ask natural language questions about document content
✔ Uses semantic search instead of keyword matching
✔ Generates context-aware answers using LLMs
✔ Prevents hallucinations by answering only from document context
✔ Simple and interactive Streamlit web interface

🧠 Tech Stack
Technology	Purpose
Python	Core programming language
Streamlit	Web interface
LangChain	RAG pipeline orchestration
FAISS	Vector database for similarity search
Sentence Transformers	Text embeddings
HuggingFace Transformers (FLAN-T5)	Language model for answer generation
PyPDFLoader	Extracting text from PDF documents
🏗 System Architecture
User Uploads PDF
        │
        ▼
Text Extraction (PyPDFLoader)
        │
        ▼
Text Chunking (RecursiveCharacterTextSplitter)
        │
        ▼
Embeddings Generation (Sentence Transformers)
        │
        ▼
Vector Storage (FAISS)
        │
        ▼
Retriever (Top-K Similarity Search)
        │
        ▼
LLM (FLAN-T5)
        │
        ▼
Context-Based Answer

This architecture ensures that answers are accurate, contextual, and grounded in the uploaded document.

📸 Example Use Cases

• Resume analysis
• Research paper querying
• Legal document analysis
• Knowledge base search
• Study material Q&A

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/ai-document-qa.git
cd ai-document-qa
2️⃣ Create virtual environment
python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install streamlit langchain faiss-cpu sentence-transformers transformers torch pypdf
▶️ Running the Application
streamlit run app.py

Open the browser:

http://localhost:8501

Upload a PDF and start asking questions.

💡 Example Questions
What is the CGPA of the candidate?
Which technologies are mentioned in the document?
What projects are listed in the resume?
What skills are highlighted in the document?
📂 Project Structure
AI-Document-QA
│
├── app.py
├── README.md
├── requirements.txt
└── sample_documents
    └── sample.pdf
🎯 Learning Outcomes

Through this project:

• Implemented a Retrieval-Augmented Generation (RAG) pipeline
• Learned how vector databases enable semantic search
• Integrated LLMs with document retrieval systems
• Built a real-world AI application using modern ML tools

👨‍💻 Author

Sampark Gupta
B.Tech Computer Science
Chandigarh University
