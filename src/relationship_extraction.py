# relationship_extraction.py
"""
Phase 4: Relationship Extraction

This script loads the hybrid NER model (ML + rule-based), processes a cleaned resume,
and extracts high-confidence relationships between entities using spaCy dependency parsing.
"""

import spacy
import os

MODEL_PATH = "./custom_ner_model_with_rules"
SAMPLE_PATH = "./extracted_texts/resume_temp.txt"

if not os.path.exists(MODEL_PATH):
    print("[ERROR] Model not found.")
    exit()

nlp = spacy.load(MODEL_PATH)

if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")

if not os.path.exists(SAMPLE_PATH):
    print("[ERROR] Resume text not found.")
    exit()

with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    text = file.read().strip()

if not text:
    print("[WARNING] Empty resume file.")
    exit()

doc = nlp(text)

entities = [(ent.text, ent.label_) for ent in doc.ents]
print("\nNamed Entities Detected:")
for text, label in entities:
    print(f"- {text} ({label})")

print("\nDetected Relationships:")

# Clean filters
ignore_designations = {"DETAILS", "Drawn Salary", "projections, etc", "Key Responsibilities"}
invalid_skills = {"Maintain", "Manage", "cash", "company", "Melaka", "P&L", "notices", "covenants,"}
ignore_names = {"TECHNICAL SKILLS", "LANGUAGE SKILLS", "EDUCATION DETAILS", "Key Responsibilities",
                 "PROFESSIONAL EXPERIENCE", "Company Secretary", "Public Accountant", "Accounts Executive"}

# Relationship 1: NAME → SKILLS
for sent in doc.sents:
    name = None
    skills = []
    for ent in sent.ents:
        if ent.label_ == "NAME" and ent.text not in ignore_names and 2 <= len(ent.text.split()) <= 3:
            name = ent.text.strip()
        elif ent.label_ == "SKILLS" and ent.text not in invalid_skills:
            skills.append(ent.text.strip())
    if name and skills:
        for skill in skills:
            print(f"{name} → has_skill → {skill}")

# Relationship 2: DESIGNATION → ORG
for sent in doc.sents:
    title = None
    orgs = []
    for ent in sent.ents:
        if ent.label_ == "DESIGNATION" and ent.text not in ignore_designations:
            title = ent.text.strip()
        elif ent.label_ == "SKILLS" and ent.text.strip() not in invalid_skills:
            orgs.append(ent.text.strip())
    if title and orgs:
        for org in orgs:
            print(f"{title} → at → {org}")
