# Phase 4: Relationship Extraction (Consolidated)

"""
This single script performs relationship extraction using two strategies:
1. Rule-based filtering based on NER results.
2. DependencyMatcher using spaCy’s dependency parser from `en_core_web_sm`.

It uses the trained NER model from Phase 3 for entity recognition, and a secondary POS-tagged model
for syntactic relationship extraction.
"""

import spacy
import os
import json
from spacy.matcher import DependencyMatcher

CUSTOM_MODEL_PATH = "./output/model-best"
SAMPLE_PATH = "./extracted_texts/resume_temp.txt"
GROUND_TRUTH_PATH = "./src/phase_4_ground_truth.json"

if not os.path.exists(CUSTOM_MODEL_PATH):
    print("[ERROR] Trained NER model not found.")
    exit()

if not os.path.exists(SAMPLE_PATH):
    print("[ERROR] Resume text file not found.")
    exit()

custom_nlp = spacy.load(CUSTOM_MODEL_PATH)
if "sentencizer" not in custom_nlp.pipe_names:
    custom_nlp.add_pipe("sentencizer")

dep_nlp = spacy.load("en_core_web_sm")

with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    text = file.read().strip()

if not text:
    print("[WARNING] Resume text is empty.")
    exit()

# Process text through both models
doc_ner = custom_nlp(text)
doc_dep = dep_nlp(text)

extracted_relationships = []

print("\nNamed Entities Detected:")
for ent in doc_ner.ents:
    print(f"- {ent.text} ({ent.label_})")

print("\nRule-Based Relationships:")
ignore_designations = {"DETAILS", "Drawn Salary", "projections, etc", "Key Responsibilities"}
invalid_skills = {"Maintain", "Manage", "cash", "company", "Melaka", "P&L", "notices", "covenants,"}
ignore_names = {"TECHNICAL SKILLS", "LANGUAGE SKILLS", "EDUCATION DETAILS", "Key Responsibilities",
                "PROFESSIONAL EXPERIENCE", "Company Secretary", "Public Accountant", "Accounts Executive"}

for sent in doc_ner.sents:
    name = None
    skills = []
    for ent in sent.ents:
        if ent.label_ == "NAME" and ent.text not in ignore_names and 2 <= len(ent.text.split()) <= 3:
            name = ent.text.strip()
        elif ent.label_ == "SKILLS" and ent.text not in invalid_skills and len(ent.text.strip()) > 1:
            skills.append(ent.text.strip())
    if name and skills:
        for skill in skills:
            extracted_relationships.append({"head": name, "relation": "has_skill", "tail": skill})
            print(f"{name} → has_skill → {skill}")

for sent in doc_ner.sents:
    title = None
    orgs = []
    for ent in sent.ents:
        if ent.label_ == "DESIGNATION" and ent.text not in ignore_designations:
            title = ent.text.strip()
        elif ent.label_ == "SKILLS" and ent.text.strip() not in invalid_skills and len(ent.text.strip()) > 1:
            orgs.append(ent.text.strip())
    if title and orgs:
        for org in orgs:
            extracted_relationships.append({"head": title, "relation": "at", "tail": org})
            print(f"{title} → at → {org}")

print("\nDependency-Based Relationships:")
matcher = DependencyMatcher(dep_nlp.vocab)

employment_patterns = [
    [
        {"RIGHT_ID": "verb", "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"IN": ["work", "join", "serve"]}}},
        {"LEFT_ID": "verb", "REL_OP": ">", "RIGHT_ID": "subject", "RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "verb", "REL_OP": ">", "RIGHT_ID": "object", "RIGHT_ATTRS": {"DEP": "dobj"}}
    ],
    [
        {"RIGHT_ID": "verb", "RIGHT_ATTRS": {"LEMMA": "hire", "POS": "VERB"}},
        {"LEFT_ID": "verb", "REL_OP": ">", "RIGHT_ID": "passive_subj", "RIGHT_ATTRS": {"DEP": "nsubj:pass"}},
        {"LEFT_ID": "verb", "REL_OP": ">", "RIGHT_ID": "agent", "RIGHT_ATTRS": {"DEP": "agent"}}
    ],
    [
        {"RIGHT_ID": "cop", "RIGHT_ATTRS": {"LEMMA": "be", "POS": "AUX"}},
        {"LEFT_ID": "cop", "REL_OP": ">", "RIGHT_ID": "subject", "RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "cop", "REL_OP": ">", "RIGHT_ID": "position", "RIGHT_ATTRS": {"DEP": "attr"}}
    ],
    [
        {"RIGHT_ID": "led", "RIGHT_ATTRS": {"LEMMA": "lead", "POS": "VERB"}},
        {"LEFT_ID": "led", "REL_OP": ">", "RIGHT_ID": "person", "RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "led", "REL_OP": ">", "RIGHT_ID": "team", "RIGHT_ATTRS": {"DEP": "dobj"}}
    ],
    [
        {"RIGHT_ID": "managed", "RIGHT_ATTRS": {"LEMMA": "manage", "POS": "VERB"}},
        {"LEFT_ID": "managed", "REL_OP": ">", "RIGHT_ID": "person", "RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "managed", "REL_OP": ">", "RIGHT_ID": "target", "RIGHT_ATTRS": {"DEP": "dobj"}}
    ],
    [
        {"RIGHT_ID": "served", "RIGHT_ATTRS": {"LEMMA": "serve", "POS": "VERB"}},
        {"LEFT_ID": "served", "REL_OP": ">", "RIGHT_ID": "person", "RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "served", "REL_OP": ">", "RIGHT_ID": "role", "RIGHT_ATTRS": {"DEP": "prep"}}
    ]
]

matcher.add("employment_relation", employment_patterns)

matches = matcher(doc_dep)
for match_id, token_ids in matches:
    tokens = [doc_dep[i] for i in token_ids]
    if len(tokens) == 3:
        head, relation, tail = tokens[1].text, tokens[0].text, tokens[2].text
        extracted_relationships.append({"head": head, "relation": relation, "tail": tail})
        print(f"{head} → {relation} → {tail}")

# Evaluation Section
if os.path.exists(GROUND_TRUTH_PATH):
    with open(GROUND_TRUTH_PATH, "r") as f:
        ground_truth = json.load(f)

    correct = 0
    for truth in ground_truth:
        if truth in extracted_relationships:
            correct += 1

    precision = correct / len(extracted_relationships) if extracted_relationships else 0
    recall = correct / len(ground_truth) if ground_truth else 0

    print("\nEvaluation Results:")
    print(f"Total Extracted: {len(extracted_relationships)}")
    print(f"Total Ground Truth: {len(ground_truth)}")
    print(f"Correct Matches: {correct}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
else:
    print("[INFO] Ground truth file not found. Skipping evaluation.")
