"""
Step 3: Train Custom Entity Recognition Model(phase 3)

This script trains a custom spaCy model using your labeled training data
from training_data.py and your defined entity labels.

The model will learn to recognize entities like NAME, EMAIL, PHONE, etc.,
and will be saved to the ./custom_ner_model directory for future use.
"""

import spacy
from spacy.training.example import Example
from spacy.util import minibatch, compounding
import random
import os

# Load your annotated training data
from training_data import TRAINING_DATA

# Create a blank English model
nlp = spacy.blank("en")

# Add NER pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Add custom labels from training data
for _, annotations in TRAINING_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable other pipeline components during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

# Training loop
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for iteration in range(40):
        print(f"Iteration {iteration + 1}...")
        random.shuffle(TRAINING_DATA)
        batches = minibatch(TRAINING_DATA, size=compounding(4.0, 32.0, 1.5))
        for batch in batches:
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], sgd=optimizer)

# Save the trained model to disk
output_dir = "./custom_ner_model"
os.makedirs(output_dir, exist_ok=True)
nlp.to_disk(output_dir)
print(f"\n✅ Model trained and saved to {output_dir}")



# TESTING THE MODEL
print("\n📌 Running test on a sample input using the trained model:")

# Load the saved model
loaded_model = spacy.load(output_dir)

# Provide a sentence the model hasn't seen before
test_text = "John Doe developed a web application using Django and React."

doc = loaded_model(test_text)
print("\nEntities detected:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})")
