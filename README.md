# 📌 Resume Parser with ML & NLP

## 🎯 Project Objective
This project is a modular resume parsing system that:
- Extracts structured data from raw resumes (`PDF`, `DOCX`, `Images`)
- Uses **custom-trained spaCy NER**
- Stores results in SQL Server
- Prepares cleaned data for downstream **machine learning applications**

---

## 🧱 Phased Approach & Techniques

### Phase 1: Data Extraction
- Tools: `python-docx`, `PyMuPDF`, `pytesseract`
- Extracted text from `.docx`, `.pdf`, and image-based resumes.

### Phase 2: Data Cleaning
- Used regular expressions to normalize whitespace, remove headers/footers, and correct formatting issues.

### Phase 3: Annotation & Conversion
- Manually labeled training data with entity spans.
- Converted annotations into `.spacy` format using `DocBin`.

### Phase 4: Named Entity Recognition (NER)
- Trained a **custom spaCy model** to recognize:
  - `PERSON`, `EMAIL`, `PHONE`, `EDUCATION`, `INSTITUTION`, `SKILLS`, `PROJECT`, `DESIGNATION`
- Incorporated fallback logic for email/phone/name via regex or keyword matching.

### Phase 5: Data Integration with SQL Server
- Designed and created a normalized SQL schema:
  - Tables: `candidates`, `skills`, `education`, `contact_info`, `experiences`
- Used `pyodbc` to insert resume data with **duplicate checking and error handling**
- Logged success/failure of each file processed

### Phase 6: Data Modeling & ML
- Queried structured data using `pandas.read_sql()`
- Aggregated and encoded skills using `MultiLabelBinarizer`
- Performed clustering with `KMeans`
- Trained a **Random Forest classifier** to predict job titles
- Implemented **similarity search** using cosine similarity on encoded skill vectors

---

## 🧪 Evaluation Criteria

| Metric         | Evaluation                                                                 |
|----------------|----------------------------------------------------------------------------|
| NER Quality     | Evaluated on test text + entity-level fallback logic                     |
| SQL Schema      | Fully normalized; no redundancy; truncation-proof                        |
| Data Insertion  | Robust, deduplicated, log-tracked                                         |
| ML Readiness    | Clean, one-row-per-candidate format with binary skill features           |
| Export Utility  | CSV outputs (`clean_resume_data.csv`, `encoded_resume_data.csv`) created |

---

## ✅ Project Outcomes
- A complete NLP-to-SQL-to-ML pipeline
- Accurate entity extraction and SQL data storage
- Batch processing of resumes with duplicate avoidance
- Clean machine learning input dataset
- Top-matching resume suggestions via cosine similarity

---


---

## 🧭 Next Steps
- Add job-role matching by skill overlap
- Expand annotated data for better NER generalization
- Build an interactive frontend (Streamlit / Power BI dashboard)

---




