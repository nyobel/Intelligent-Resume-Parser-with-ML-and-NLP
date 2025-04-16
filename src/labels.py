"""
step 1: Define Custom Entity Labels(phase 3)

This file stores the list of entity types that are to be in the NER model to learn and extract from resume text.

These labels will guide the annotation process and training of our custom model.
"""

ENTITY_LABELS = [
    "NAME",
    "EMAIL",
    "PHONE",
    "EDUCATION",
    "SKILLS",
    "EXPERIENCE",
    "DESIGNATION",
    "PROJECT"
]
