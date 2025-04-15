"""
Extract text from DOCX resumes using python-docx.

"""

import os
from docx import Document # library to read .docx word documents

def extract_text_from_docx(filepath: str) -> str:
    """
    Extracts text from a DOCX file.
    Args:
        filepath (str): Path to the .docx file
    Returns:
        str: Extracted plain text from the document
    """

    text = ""
    try:
        doc = Document(filepath) # open the .docx file

        # collect non-empty paragraphs into a single text block
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text += paragraph.text + "\n"

        print(f"[INFO] Successfully extracted text from: {os.path.basename(filepath)}")
    except Exception as e:
        # log errors that may occur during reading
        print(f"[ERROR] Failed to read {filepath}: {e}")


    return text.strip() #return clean, plain text

# Test the function
if __name__ == "__main__":
    test_path = "./data/sample_resumes/resume_temp.docx" 
    if os.path.exists(test_path):
        result = extract_text_from_docx(test_path)
        print("\nExtracted Text Preview:\n", result[:1000], "...\n")  # Print first 1000 characters
    else:
        print("[ERROR] Test DOCX file not found. Please check the path.")