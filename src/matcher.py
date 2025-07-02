from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ResumeMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.job_vectors = None

    def fit(self, job_descriptions: List[str]):
        """
        Fit the matcher on job descriptions.
        """
        self.job_vectors = self.vectorizer.fit_transform(job_descriptions)

    def match(self, resumes: List[str]) -> np.ndarray:
        """
        Compute cosine similarity between resumes and job descriptions.

        Returns:
            np.ndarray: A matrix of similarity scores (resumes x job_descriptions)
        """
        resume_vectors = self.vectorizer.transform(resumes)
        return cosine_similarity(resume_vectors, self.job_vectors)
