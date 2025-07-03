import streamlit as st
import sys
import os
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 👇 Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import extract_text_from_docx, extract_text_from_pdf, extract_text_from_txt
from src.preprocessing import preprocess_text
from src.llm_utils import ask_mistral, get_resume_feedback
from src.semantic_matcher import compute_similarity

st.write("✅ Import successful")

st.set_page_config(page_title="SmartHire AI", layout="centered")

st.title("📄 SmartHire: AI Resume Matcher")

# Helper to handle all 3 file types
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        return extract_text_from_txt(uploaded_file)
    else:
        return "Unsupported file format."

uploaded_files = st.file_uploader("📎 Upload Resumes", type=["pdf", "docx", "txt"], accept_multiple_files=True)
job_desc = st.text_area("💼 Paste Job Description", height=300)

if uploaded_files and job_desc:
    jd_cleaned = preprocess_text(job_desc)
    resume_texts = []
    resume_names = []
    raw_resumes = []
    for file in uploaded_files:
        text = extract_text_from_file(file)
        cleaned = preprocess_text(text)
        resume_texts.append(cleaned)
        resume_names.append(file.name)
        raw_resumes.append(text)

    scores = compute_similarity(resume_texts, jd_cleaned)

    ranked =sorted(zip(resume_names, scores, uploaded_files, raw_resumes), key=lambda x: x[1], reverse=True)

    st.subheader("📊 Ranked Resumes (by Semantic Match)")
    for i, (name, score, file, raw_text) in enumerate(ranked):
        st.markdown(f"**{i+1}. {name}** — Match Score: `{score:.2f}`")
        with st.expander("📄 View Resume"):
            st.text(raw_text[:2000] + ("..." if len(raw_text) > 2000 else ""))

    with st.spinner("💬 Analyzing top resume using LLM..."):
        feedback = get_resume_feedback(ranked[0][3], job_desc)

    st.markdown("### 💡 LLM Feedback")
    st.write(feedback)

# 🔎 Freeform Query Section
st.markdown("---")
st.subheader("🔎 Ask a Semantic Question (e.g., 'Who has AWS experience?')")

query = st.text_input("Enter your question")

if query:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec = model.encode([query])
    resume_vecs = model.encode(resume_texts)

    similarities = cosine_similarity(resume_vecs, query_vec).flatten()
    ranked_query = sorted(zip(resume_names, similarities, raw_resumes), key=lambda x: x[1], reverse=True)

    st.markdown("### 🧠 Query Results:")
    for i, (name, score, resume_text) in enumerate(ranked_query):
        if score < 0.4:
            continue

        st.markdown(f"**{name}** — Relevance: `{score:.2f}`")
        with st.expander("📄 View Resume"):
            st.text(resume_text[:2000] + ("..." if len(resume_text) > 2000 else ""))

        if st.button(f"🧠 Ask Mistral about {name}", key=f"mistral_query_{i}"):
            with st.spinner("Thinking with Mistral..."): 
                response = ask_mistral(resume_text, query)
                st.markdown("#### 💬 Mistral's Insight")
                st.write(response)


