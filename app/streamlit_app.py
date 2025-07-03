import streamlit as st
import sys
import os

# 👇 Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import extract_text_from_docx, extract_text_from_pdf, extract_text_from_txt
from src.preprocessing import preprocess_text
from src.matcher import ResumeMatcher
from src.llm_utils import get_resume_feedback

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

resume_file = st.file_uploader("📎 Upload Resume", type=["pdf", "docx", "txt"])
job_desc = st.text_area("💼 Paste Job Description", height=300)

if resume_file and job_desc:
    resume_text = extract_text_from_file(resume_file)
    resume_cleaned = preprocess_text(resume_text)
    jd_cleaned = preprocess_text(job_desc)

    matcher = ResumeMatcher()
    matcher.fit([jd_cleaned])
    score = matcher.match([resume_cleaned])[0][0]

    st.markdown(f"### ✅ Similarity Score: **{score:.2f}**")

    with st.spinner("💬 Analyzing resume using LLM..."):
        feedback = get_resume_feedback(resume_text, job_desc)

    st.markdown("### 💡 LLM Feedback")
    st.write(feedback)
