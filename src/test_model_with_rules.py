# test_model_with_rules.py
"""
Test the upgraded spaCy model with rule-based EntityRuler.
This version loads the saved model from custom_ner_model_with_rules
and runs it on a single test resume to show both ML and rule-based detections.
"""

import spacy
import os

model_path = "./custom_ner_model_with_rules"
sample_path = "./extracted_texts/resume_2_pdf.txt"  # Change if needed

# Load the model with rules
if not os.path.exists(model_path):
    print("Error: Updated model with rules not found.")
    exit()

nlp = spacy.load(model_path)

# Load test resume
if not os.path.exists(sample_path):
    print("Error: Sample resume not found.")
    exit()

with open(sample_path, "r", encoding="utf-8") as file:
    text = file.read()

# Run entity recognition
doc = nlp(text)

print("\nEntities detected with rule-enhanced model:\n")
for ent in doc.ents:
    print(f"- {ent.text}  ({ent.label_})")
