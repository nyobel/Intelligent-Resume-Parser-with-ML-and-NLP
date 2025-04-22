import spacy

nlp = spacy.load("output/model-best")

text = "Mercy Chebet is a Software Engineer with a BSc in Computer Science from the University of Nairobi. She can be reached at mercy.k@cloudmail.com or +254-701-123456. She built a resume parser using spaCy and designed an HR analytics dashboard using Power BI. She's skilled in Python, React, and SQL."

doc = nlp(text)

print("📌 Detected Entities:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})")

