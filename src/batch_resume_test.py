# phase_3_batch_resume_test.py
"""
Test your trained custom NER model across all extracted resume .txt files.
This script loads the saved model, processes each file in ./extracted_texts,
and prints the entities detected in each.
"""

import spacy
import os

model_path = "./custom_ner_model"
resumes_dir = "./extracted_texts"

# Check if model exists
if not os.path.exists(model_path):
    print("Error: Trained model not found.")
    exit()

# Load model
nlp = spacy.load(model_path)

# Loop through .txt resumes in extracted_texts folder
print("\nBatch Entity Detection Across Resumes:\n")

for filename in os.listdir(resumes_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(resumes_dir, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read().strip()

        if not text:
            print(f"{filename}: [Empty File]\n")
            continue

        doc = nlp(text)

        print(f"{filename}:")
        if doc.ents:
            for ent in doc.ents:
                print(f"- {ent.text} ({ent.label_})")
        else:
            print("- No entities detected.")
        print("\n" + "-" * 50 + "\n")
