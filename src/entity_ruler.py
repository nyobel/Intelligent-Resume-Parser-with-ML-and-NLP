# add_entity_ruler.py
"""
This script adds rule-based entity patterns to your trained spaCy model.
It uses a JSONL file of patterns and injects them using EntityRuler.
The final model combines both rule-based and ML-predicted entities.
"""

import spacy
import os

# Path to the original trained model
base_model_path = "./custom_ner_model"
# Path to the enhanced model that will include rule-based logic
updated_model_path = "./custom_ner_model_with_rules"
# Path to the pattern rules
patterns_path = "./src/entity_patterns.jsonl"

# Load your existing trained NER model
print("Loading base model from:", base_model_path)
nlp = spacy.load(base_model_path)

# Add the EntityRuler by name (registered component)
print("Adding entity_ruler to pipeline before 'ner'")
nlp.add_pipe("entity_ruler", before="ner")

# Load the actual patterns into the ruler
print("Loading patterns from:", patterns_path)
ruler = nlp.get_pipe("entity_ruler")
ruler.from_disk(patterns_path)

# Save the new model with rules
os.makedirs(updated_model_path, exist_ok=True)
nlp.to_disk(updated_model_path)
print(f"✅ Model with rule-based patterns saved to: {updated_model_path}")
