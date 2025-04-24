import spacy

nlp = spacy.load("output/model-best")

text = """Mercy Chebet is a Software Engineer with a BSc in Computer Science from the University of Nairobi. 
She can be reached at mercy.k@cloudmail.com or +254-701-123456. 
She built a resume parser using spaCy and designed an HR analytics dashboard using Power BI. 
She's skilled in Python, React, and SQL."""



doc = nlp(text)

print("📌 Detected Entities:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})")


# converting ner to dictionary
from phase_5_ner_to_dict import ner_to_dict

structured = ner_to_dict(doc)
print("\n📦 Structured Output:")
for k, v in structured.items():
    print(f"{k}: {v}")


from phase_5_ner_to_dict import ner_to_dict
from phase_5_populate_resume_data import insert_candidate_data

# Load model
import spacy
nlp = spacy.load("output/model-best")

# Resume text input
text = """Mercy Chebet is a Software Engineer with a BSc in Computer Science from the University of Nairobi.
She can be reached at mercy.k@cloudmail.com or +254-701-123456.
She built a resume parser using spaCy and designed an HR analytics dashboard using Power BI.
She's skilled in Python, React, and SQL."""

# Run model and insert
doc = nlp(text)
structured = ner_to_dict(doc)
insert_candidate_data(structured)
