import os
from typing import Dict
from docx import Document
import fitz
import PyPDF2
from pathlib import Path

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text

def extract_text_from_docx(uploaded_file) -> str:  # Extract text from a DOCX file
    doc = Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(uploaded_file) -> str:  # Extract text from a TXT file
    return uploaded_file.read().decode("utf-8")

def load_resumes(folder_path: str) -> Dict[str, str]:
    resume_texts = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith('.pdf'):
            resume_texts[filename] = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            resume_texts[filename] = extract_text_from_docx(file_path)
        elif filename.endswith('.txt'):
            resume_texts[filename] = extract_text_from_txt(file_path)
    return resume_texts

def load_job_descriptions(folder_path: str) -> Dict[str, str]:
    jd_texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            jd_texts[filename] = extract_text_from_txt(file_path)
    return jd_texts