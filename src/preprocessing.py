import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    text = text.lower()  # Lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # Remove non-alphabetic characters

    # Process the text with spaCy
    doc = nlp(text)

    # Tokenize and remove stopwords, punctuation, and non-alphabetic tokens
    filtered_tokens = [
        token.text for token in doc
        if token.text not in STOP_WORDS and token.is_alpha
    ]

    return ' '.join(filtered_tokens)
