import re
import PyPDF2
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

# Download NLTK stopwords
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF resume."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def preprocess_text(text):
    """Cleans text by removing stopwords, special characters, and extra spaces."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)  # Remove special characters
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]
    return " ".join(words)

def extract_keywords(resume_text, job_desc, top_n=10):
    """Extracts top matching keywords from the resume based on job description."""
    documents = [resume_text, job_desc]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Get feature names and sort by importance
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]  # Resume scores
    
    # Create DataFrame
    keyword_df = pd.DataFrame({'Keyword': feature_names, 'Score': scores})
    keyword_df = keyword_df.sort_values(by="Score", ascending=False)
    
    return keyword_df.head(top_n)['Keyword'].tolist()
