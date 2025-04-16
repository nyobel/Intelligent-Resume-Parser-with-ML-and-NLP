import os  # Provides functions to interact with the operating system (e.g., file paths, directories)

# Import the specific extraction functions for each file type
from extract_pdf import extract_text_from_pdf
from extract_docx import extract_text_from_docx
from extract_image import extract_text_from_image

def extract_resume_text(filepath: str) -> str:
    """
    Determines the file type based on extension and routes the file to the
    appropriate extraction method.

    Args:
        filepath (str): The full path to the resume file

    Returns:
        str: Extracted plain text from the resume
    """
    ext = os.path.splitext(filepath)[1].lower()  # Get the file extension in lowercase
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext == ".docx":
        return extract_text_from_docx(filepath)
    elif ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(filepath)
    else:
        print(f"[WARN] Unsupported file type: {filepath}")
        return ""  # Return an empty string if unsupported

def save_text_to_file(text: str, output_path: str):
    """
    Saves the extracted text into a .txt file.

    Args:
        text (str): The extracted resume text
        output_path (str): Where the .txt file should be saved
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    """
    Main driver function:
    - Reads all files from the sample_resumes folder
    - Extracts text from each using the appropriate method
    - Saves the extracted text as .txt files in extracted_texts folder
    """
    input_dir = "./data/sample_resumes"          # Folder containing input resumes
    output_dir = "./extracted_texts"              # Folder to save extracted .txt files
    os.makedirs(output_dir, exist_ok=True)         # Create the output folder if it doesn't exist

    for filename in os.listdir(input_dir):         # Loop through each file in the input folder
        filepath = os.path.join(input_dir, filename)
        print(f"\n[PROCESSING] {filename}")

        extracted = extract_resume_text(filepath)  # Call extractor function based on file type

        if extracted:
            output_filename = os.path.splitext(filename)[0] + ".txt"  # Create a new .txt file name
            output_path = os.path.join(output_dir, output_filename)
            save_text_to_file(extracted, output_path)  # Save the extracted text
            print(f"[SAVED] Extracted text to {output_path}")
        else:
            print("[SKIPPED] No text extracted.")

# Entry point for the script
if __name__ == "__main__":
    main()
