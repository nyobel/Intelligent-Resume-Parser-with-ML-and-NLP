"""
Phase 1: Resume Data Extraction
Objective: Extract raw text from various resume formats (PDF, DOCX, PNG) into plain text files for further processing.
"""

import os
from typing import Union

# Import extractors
from extract_pdf import extract_text_from_pdf
from extract_docx import extract_text_from_docx
from extract_image import extract_text_from_image

def extract_resume_text(filepath: str) -> Union[str, None]:
    """Detects file type and applies appropriate extraction method."""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext == ".docx":
        return extract_text_from_docx(filepath)
    elif ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(filepath)
    else:
        print(f"Unsupported file type: {ext}")
        return None

def save_text_to_file(text: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    input_dir = "data/sample_resumes"
    output_dir = "extracted_texts"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        print(f"Processing {filename}...")
        extracted = extract_resume_text(filepath)
        if extracted:
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
            save_text_to_file(extracted, output_file)
            print(f"Saved extracted text to {output_file}\n")
        else:
            print("Extraction failed.\n")
