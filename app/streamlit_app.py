import streamlit as st
import sys
import os

# 👇 Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import extract_text_from_docx, extract_text_from_pdf, extract_text_from_txt
from src.preprocessing import preprocess_text
from src.llm_utils import get_resume_feedback
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
    for file in uploaded_files:
        text = extract_text_from_file(file)
        cleaned = preprocess_text(text)
        resume_texts.append(cleaned)
        resume_names.append(file.name)

    scores = compute_similarity(resume_texts, jd_cleaned)

    ranked =sorted(zip(resume_names, scores, uploaded_files), key=lambda x: x[1], reverse=True)

    st.subheader("📊 Ranked Resumes (by Semantic Match)")
    for i, (name, score, file) in enumerate(ranked):
        st.markdown(f"**{i+1}. {name}** — Match Score: `{score:.2f}`")
        with st.expander("📄 View Resume"):
            st.text(extract_text_from_file(file)[:2000] + ("..." if file.size > 2000 else ""))
            
    st.markdown(f"### 🔍 Semantic Similarity Score: **{scores:.2f}**")

    with st.spinner("💬 Analyzing resume using LLM..."):
        feedback = get_resume_feedback(resume_texts, job_desc)

    st.markdown("### 💡 LLM Feedback")
    st.write(feedback)
