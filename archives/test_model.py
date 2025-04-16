"""
Test your trained custom NER model on real extracted resume text.
Make sure you've already trained and saved the model in ./custom_ner_model
"""

import spacy
import os

model_path = "./custom_ner_model"
resume_path = "./extracted_texts/resume_2_pdf.txt"  # Change if needed

try:
    # Check for trained model
    if not os.path.exists(model_path):
        raise FileNotFoundError("Trained model not found. Please train it first.")

    # Load model
    nlp = spacy.load(model_path)

    # Check for resume file
    if not os.path.exists(resume_path):
        raise FileNotFoundError("Resume file not found. Please check the path.")

    # Read resume content
    with open(resume_path, "r", encoding="utf-8") as file:
        resume_text = file.read()

    if not resume_text.strip():
        raise ValueError("The resume file is empty.")

    # Run the model on resume text
    doc = nlp(resume_text)

    # Show results
    if doc.ents:
        print("\nEntities detected in resume:\n")
        for ent in doc.ents:
            print(f"- {ent.text} -> ({ent.label_})")
    else:
        print("\nNo entities detected in the resume.")

except FileNotFoundError as fnf_error:
    print(f"{fnf_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
