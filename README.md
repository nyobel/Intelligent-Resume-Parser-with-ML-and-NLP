# Resume Parser with ML and NLP

## Project Overview
This project is a resume parsing system that extracts structured information from resumes using a combination of **Machine Learning** and **Rule-Based Named Entity Recognition (NER)**. The goal is to transform unstructured resumes in PDF, DOCX, and image formats into structured data for downstream applications like applicant screening, skill matching, and job recommendation systems.

---

##  Project Structure

```
INTELLIGENT RESUME PARSER WITH ML AND NLP/
│
├── archives/                          # Archived experiments and backup models
├── data/                              # Source resume files
├── extracted_texts/                   # Cleaned text files extracted from resumes
├── output/                            # Trained model and artifacts
│
├── src/                               # Project logic (all Python scripts)
│   ├── __pycache__/
│   ├── entity_patterns.jsonl          # Optional pattern file (unused in training)
│   ├── extract_docx.py                # DOCX extractor
│   ├── extract_image.py               # OCR for image resumes
│   ├── extract_pdf.py                 # PDF extractor
│   ├── labels.py                      # Custom entity label definitions
│   ├── phase_1_run_extraction.py      # Extracts raw text from resumes
│   ├── phase_2_data_cleaning.py       # Text normalization and cleanup
│   ├── phase_3_data_conversion.py     # Converts training data to spaCy DocBin
│   ├── phase_3_training_data.py       # Annotated training examples
│   ├── phase_4_ground_truth.json      # Ground truth triples for evaluation
│   ├── phase_4_relationship_extraction.py # Extracts rule-based and dependency-based relations
│   ├── test_model.py                  # Manual testing script for NER outputs
│
├── config.cfg                         # spaCy config for model training
├── dev.spacy                          # Dev dataset in binary format
├── train.spacy                        # Training dataset in binary format
├── requirements.txt                   # Required Python libraries
├── .gitignore                         # Files/folders to ignore in git
├── README.md                          # You are here
```

---

## Phases

### Phase 1: Data Extraction ✅
- Automatically identifies file type (PDF, DOCX, PNG/JPG)
- Extracts raw text using PyMuPDF, python-docx, or Tesseract OCR
- Saves output to `/extracted_texts/`

### Phase 2: Data Cleaning ✅
- Removes noise, lowercases, and lemmatizes
- Standardizes formatting for emails, phones, and spacing

### Phase 3: Entity Recognition (NER) ✅
- Trained a custom NER model using **spaCy** and labeled training data
- No `EntityRuler` was used
- Labels include: `NAME`, `EMAIL`, `PHONE`, `EDUCATION`, `DESIGNATION`, `SKILLS`, `EXPERIENCE`, `PROJECT`

### Phase 4: Relationship Extraction ✅
- Uses both rule-based and dependency-based methods
- Extracts triplets such as:
  - `NAME → has_skill → SKILL`
  - `DESIGNATION → at → ORG`
  - `PERSON → joined → ORG`
  - `PERSON → was → DESIGNATION`

---

## ⚠️ Current Challenge: Entity Label Inconsistencies

Despite the hybrid approach, the NER output still suffers from **misclassification**:
- trouble identifying `NAME` as an entity

### Examples:
- `Vasanthi` → labeled as `SKILLS` instead of `NAME`
- `Microsoft Office` → labeled as `NAME` instead of `SKILLS`
- `DETAILS` → labeled as `DESIGNATION`
- `Bank`, `Melaka` → labeled as `SKILLS`, though they are locations or organizations

### What's Been Done:
- Trained ML model with contextual variety
- Used logic filters to ignore commonly misclassified terms
- Evaluated relationships against a curated `ground_truth` JSON

---

## Installation

```bash
pip install -r requirements.txt
python -m nltk.downloader punkt stopwords wordnet
python -m spacy download en_core_web_sm
```

---

## ✅ Running the Project

```bash
# Extract text from resumes
python src/phase_1_run_extraction.py

# Clean and normalize extracted text
python src/phase_2_data_cleaning.py

# Convert training data
python src/phase_3_data_conversion.py

# Train ML NER model
python -m spacy train config.cfg --output output --paths.train train.spacy --paths.dev dev.spacy

# Run relationship extraction
python src/phase_4_relationship_extraction.py
```

---
## Status
- Phase 1–4 completed and tested
- Phase 5 (Data Integration) coming next
