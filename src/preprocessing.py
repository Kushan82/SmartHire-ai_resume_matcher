import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stopwords = set(stopwords.words('english'))

def preprocess_text(text:str) -> str:
    text = text.lower()  # Convert to lowercase

    text= re.sub(r'[^a-z\s]','',text) # Remove non-alphabetic characters

    tokens = word_tokenize(text)  # Tokenize the text

    filtered_tokens =[word for word in tokens if word not in stopwords]  # Remove stopwords

    return ' '.join(filtered_tokens)  # Join tokens back into a string


    