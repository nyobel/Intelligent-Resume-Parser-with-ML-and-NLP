"""
Extract text from image-based resumes using OCR (Tesseract).

"""

import os
import cv2
import pytesseract
from PIL import Image

# Specify the path to the tesseract executable if not in PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_text_from_image(filepath: str) -> str:
    """
    Extracts text from image using OCR.
    Args:
        filepath (str): Path to image file (.png, .jpg, .jpeg)
    Returns:
        str: Extracted text
    """

    text = ""
    try:
        # Load image using OpenCV
        image = cv2.imread(filepath)

        # Convert from BGR (OpenCV default) to RGB for Tesseract
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Use pytesseract to extract text
        text = pytesseract.image_to_string(image)

        print(f"[INFO] Successfully extracted text from: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"[ERROR] Failed to extract text from {filepath}: {e}")

    return text.strip()

# Test the function
if __name__ == "__main__":
    test_path = "./data/sample_resumes/resume_1.png"
    if os.path.exists(test_path):
        result = extract_text_from_image(test_path)
        print("\nExtracted Text Preview:\n", result[:1000], "...\n")
    else:
        print("[ERROR] Test image not found. Please check the path.")
