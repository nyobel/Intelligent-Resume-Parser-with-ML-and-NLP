"""
Extract text from PDF resumes using PyMuPDF (fitz).
"""

import fitz  # PyMuPDF
import os

def extract_text_from_pdf(filepath: str) -> str:
    """Extracts text from a PDF file."""
    text = ""
    try:
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
        print(f"[INFO] Successfully extracted text from: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"[ERROR] Failed to read {filepath}: {e}")
    return text.strip()

# For quick testing (optional)
if __name__ == "__main__":
    test_path = "./data/sample_resumes/resume_1.pdf"  # Adjust path as needed
    if os.path.exists(test_path):
        result = extract_text_from_pdf(test_path)
        print("\nExtracted Text Preview:\n", result[:1000], "...\n")
    else:
        print("[ERROR] Test PDF file not found. Please check the path.")