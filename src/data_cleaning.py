"""
Phase 2: Resume Text Cleaning & Normalization

This script cleans the raw extracted resume text by:
1. Removing noise and irrelevant characters
2. Fixing formatting inconsistencies
3. Normalizing text through tokenization and lemmatization

Required installations:
    pip install nltk spacy python-dateutil
    python -m nltk.downloader punkt stopwords wordnet
    python -m spacy download en_core_web_sm
"""

import os
import re
import nltk
import spacy
from dateutil import parser as dateparser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Stopwords are common words like 'the', 'and', 'is'.
stop_words = set(stopwords.words("english"))

# Lemmatizer reduces words to their base form (running -> run, was -> be)
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Clean raw text by removing noise, normalizing whitespace, and standardizing common formats.

    Steps:
    - Remove control characters like \r, \f, \x0c
    - Remove symbols like ***, ===, etc.
    - Fix excessive line breaks and spacing
    - Normalize date formats (e.g., April 2025 → 2025-04)
    """
    text = re.sub(r'[\r\f\x0c]', ' ', text)
    text = re.sub(r'[\*\|\=\_\~]+', ' ', text)
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'\s{2,}', ' ', text)

    # Convert month-year formats into a consistent YYYY-MM format
    def fix_dates(match):
        try:
            return dateparser.parse(match.group(0)).strftime('%Y-%m')
        except:
            return match.group(0)

    text = re.sub(r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
                  r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)'
                  r'\s\d{4}\b', fix_dates, text)

    return text.strip()

def normalize_text(text):
    """
    Normalize text by:
    - Tokenizing into words
    - Removing stopwords
    - Lemmatizing each word to its base form
    - Preserving important entities like emails
    """
    # Extract full email addresses before tokenization to preserve them
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

     # Replace each email in the text with a unique placeholder (EMAILPLACEHOLDER0, etc.)
    for i, email in enumerate(emails):
        text = text.replace(email, f"EMAILPLACEHOLDER{i}") # remove email before tokenization

    try:
        # Tokenize and normalize (remove stopwords, lemmatize)
        tokens = word_tokenize(text)
        filtered = [lemmatizer.lemmatize(word.lower()) for word in tokens
                    if word.lower() not in stop_words and not re.fullmatch(r'[^a-zA-Z0-9]+', word)]

        # Convert back to string and restore email placeholders
        result = ' '.join(filtered)
        for i, email in enumerate(emails):
            result = result.replace(f"emailplaceholder{i}", email)

        return result

    except Exception as e:
        print("[ERROR] Normalization failed:", e)
        return ""

# Test with a sample resume
if __name__ == "__main__":
    sample_path = "./extracted_texts/resume_temp_2.txt"
    if os.path.exists(sample_path):
        with open(sample_path, "r", encoding="utf-8") as f:
            raw = f.read()

        print("\n[RAW EXTRACTED TEXT]\n", raw[:500], "...\n")

        cleaned = clean_text(raw)
        print("[CLEANED TEXT]\n", cleaned[:500], "...\n")

        normalized = normalize_text(cleaned)
        if normalized:
            print("[NORMALIZED TEXT]\n", normalized[:500], "...\n")
        else:
            print("[SKIPPED] Normalization returned no output.\n")
    else:
        print("Sample resume not found. Please check the path.")