from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:
    def __init__ (self):
        self.vectorizer = TfidfVectorizer()
    
    def fit(self, job_descriptions: list):
        self.job_vectors = self.vectorizer.fit_transform(job_descriptions)

    def match(self,resumes:list):
        resumes_vectors = self.vectorizer.transform(resumes)
        similarity_matrix = cosine_similarity(resumes_vectors,self.job_vectors)
        return similarity_matrix
        
        