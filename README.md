# Resume Parser with ML and NLP

## 🔍 Project Overview
This project is a resume parsing system that extracts structured information from resumes using a combination of **Machine Learning** and **Rule-Based Named Entity Recognition (NER)**. The goal is to transform unstructured resumes in PDF, DOCX, and image formats into structured data for downstream applications like applicant screening, skill matching, and job recommendation systems.

---

## 🧱 Project Structure

```
resume-parser-with-ml-and-nlp/
│
├── archives/                          # Archived models and unused test files
│
├── custom_ner_model_with_rules/      # Final working model (ML + rule patterns)
│
├── data/                              # Source resumes
├── extracted_texts/                   # Text extracted from resumes
│
├── src/                               # All Python scripts
│   ├── run_extraction.py              # Main script to extract text from resumes
│   ├── extract_pdf.py                 # Extracts text from PDF files
│   ├── extract_docx.py                # Extracts text from DOCX files
│   ├── extract_image.py               # OCR for PNG/JPG resumes
│   ├── data_cleaning.py               # Normalization, noise removal
│   ├── entity_recognition.py          # Trains the custom spaCy NER model
│   ├── entity_ruler.py                # Adds JSONL rule patterns to the model
│   ├── entity_patterns.jsonl          # All defined entity rules (EMAIL, NAME, SKILLS, etc.)
│   ├── training_data.py               # ML training data examples
│   ├── labels.py                      # Label definitions
│   ├── test_model_with_rules.py       # Tests model on a single resume
│   ├── batch_resume_test_with_rules.py# Batch NER testing across all resumes
│   ├── relationship_extraction.py     # Extracts relationships between entities
│
├── README.md                          # You are here
├── requirements.txt                   # Required Python libraries
└── .gitignore                         # Files/folders to ignore in git
```

---

## 🧠 Phases

### Phase 1: Data Extraction ✅
- Extract raw text from PDF, DOCX, and PNG resumes
- Saved to `/extracted_texts/`

### Phase 2: Data Cleaning ✅
- Normalize text, remove noise, lemmatize
- Preserve critical structures like names, emails, phone numbers

### Phase 3: Entity Recognition (NER) ✅
- Custom NER model trained on labeled data
- Enhanced with `EntityRuler` rule-based patterns for key fields:
  - `EMAIL`, `PHONE`, `EDUCATION`, `DESIGNATION`, `SKILLS`

### Phase 4: Relationship Extraction ✅
- Identify structured relationships such as:
  - `NAME → has_skill → SKILL`
  - `DESIGNATION → at → ORG`

---

## ⚠️ Current Challenge: Entity Label Inconsistencies

Despite the hybrid approach, the NER output still suffers from **misclassification**:
- trouble identifying `NAME` as an entity

### 🔴 Examples:
- `Vasanthi` → labeled as `SKILLS` instead of `NAME`
- `Microsoft Office` → labeled as `NAME` instead of `SKILLS`
- `DETAILS` → labeled as `DESIGNATION`
- `Bank`, `Melaka` → labeled as `SKILLS`, though they are locations or organizations

### 💡 What's Been Done:
- Built ML model on labeled training examples
- Added refined rule patterns for emails, phones, designations, and skills
- Applied filtering in relationship logic (e.g. ignore misfired `NAME`s)


---

## 📦 Installation
```bash
pip install -r requirements.txt
python -m nltk.downloader punkt stopwords wordnet
python -m spacy download en_core_web_sm
```

---

## ✅ Running the Project
```bash
# Extract text from resumes
python src/run_extraction.py

# Clean and normalize extracted text
python src/data_cleaning.py

# Train ML NER model
python src/entity_recognition.py

# Add rule-based patterns
python src/entity_ruler.py

# Test entity recognition
python src/test_model_with_rules.py

# Extract relationships
python src/relationship_extraction.py
```

---

## 👤 Author
Okello Crystal

## 🔧 Status
- ML+Rule model built and working
- Phase 1–4 complete
- Entity classification needs refinement
- Phase 5 (Data Integration) coming next
