from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')  # Light & fast model

def compute_similarity(resume_texts, job_description):
    """
    :param resume_texts: list of raw or preprocessed resumes
    :param job_description: string of job description
    :return: list of similarity scores (float between 0 and 1)
    """
    all_docs = resume_texts + [job_description]
    embeddings = model.encode(all_docs, convert_to_tensor=True)

    job_vec = embeddings[-1].unsqueeze(0)  # Last one is the JD
    resume_vecs = embeddings[:-1]

    sims = cosine_similarity(resume_vecs, job_vec).flatten()
    return sims
