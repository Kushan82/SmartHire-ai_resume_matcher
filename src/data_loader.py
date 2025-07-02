import os
from typing import Dict
from docx import Document
import fitz
from pathlib import Path

def extract_text_from_pdf(pdf_path: str) -> str:  # Extract text from a PDF file
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path: str) -> str:  # Extract text from a DOCX file
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(txt_path: str) -> str:  # Extract text from a TXT file
    with open(txt_path, 'r', encoding='utf-8') as f:
        return f.read()

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