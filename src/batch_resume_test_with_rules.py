# batch_resume_test_with_rules.py
"""
Batch test using the rule-enhanced spaCy model across all resume text files.
Loads model from custom_ner_model_with_rules and scans ./extracted_texts
folder to detect both rule-based and trained entities.
"""

import spacy
import os

model_path = "./custom_ner_model_with_rules"
resumes_dir = "./extracted_texts"

# Load rule-enhanced model
if not os.path.exists(model_path):
    print("Error: Updated model with rules not found.")
    exit()

nlp = spacy.load(model_path)

print("\nBatch Test - Rule-Enhanced Entity Model:\n")

for filename in os.listdir(resumes_dir):
    if filename.endswith(".txt"):
        path = os.path.join(resumes_dir, filename)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().strip()

        if not content:
            print(f"{filename}: [Empty or unreadable]\n")
            continue

        doc = nlp(content)

        print(f"{filename}:")
        if doc.ents:
            for ent in doc.ents:
                print(f"- {ent.text} ({ent.label_})")
        else:
            print("- No entities detected.")

        print("\n" + "-" * 50 + "\n")
