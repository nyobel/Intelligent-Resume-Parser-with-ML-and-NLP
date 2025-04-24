import os
import spacy
from phase_5_ner_to_dict import ner_to_dict
from phase_5_populate_resume_data import insert_candidate_data

# Load trained NER model
nlp = spacy.load("output/model-best")

# Folder containing extracted resume texts
folder_path = "extracted_texts"

# Process each .txt file
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        path = os.path.join(folder_path, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        print(f"\n📄 Processing: {filename}")
        doc = nlp(text)
        structured = ner_to_dict(doc)
        insert_candidate_data(structured)
