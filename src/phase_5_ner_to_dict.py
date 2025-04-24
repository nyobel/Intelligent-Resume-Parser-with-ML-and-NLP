import re

def ner_to_dict(doc):
    """
    Converts a spaCy Doc object into a structured Python dictionary.
    Cleans noisy entities and groups multiple skills/projects.

    Returns a dictionary ready for SQL insertion.
    """
    data = {
        "full_name": None,
        "designation": None,
        "email": None,
        "phone": None,
        "education": None,
        "institution": None,
        "skills": [],
        "project": None
    }

    # Extract entities
    for ent in doc.ents:
        label = ent.label_
        text = ent.text.strip()

        # Skip noise
        if text in [",", ".", "-", "–", "•"]:
            continue

        if label == "EMAIL":
            data["email"] = text
        elif label == "PHONE":
            data["phone"] = text
        elif label == "DESIGNATION":
            if "designations" not in data:
                data["designations"] = []
            data["designations"].append(text)
        elif label == "EDUCATION":
            if "from" in text:
                parts = text.split("from")
                data["education"] = parts[0].strip()
                data["institution"] = parts[1].strip()
            else:
                data["education"] = text
        elif label == "SKILLS":
            if text not in data["skills"]:
                data["skills"].append(text)
        elif label == "PROJECT":
            if not data["project"]:
                data["project"] = text
        elif label == "PERSON":
            if not data["full_name"]:
                data["full_name"] = text

    # Fallback: extract full name using regex (first capitalized phrase)
    if not data["full_name"]:
        match = re.search(r'^([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)', doc.text)
        if match:
            data["full_name"] = match.group(1).strip()

    # Fallback: extract phone using regex
    if not data["phone"]:
        phone_match = re.search(r'(\+?\d{3}[-\s]?\d{3}[-\s]?\d{6})', doc.text)
        if phone_match:
            data["phone"] = phone_match.group().strip()

    # Fallback: look for known skill keywords manually
    known_skills = ["Python", "SQL", "Power BI", "spaCy", "React"]
    for skill in known_skills:
        if skill.lower() in doc.text.lower() and skill not in data["skills"]:
            data["skills"].append(skill)

    # Intelligent selection of final designation
    if "designations" in data and data["designations"]:
        keyword_titles = ["engineer", "developer", "scientist", "manager", "analyst", "officer", "specialist", "consultant", "designer"]
        ranked = sorted(data["designations"], key=lambda x: any(k in x.lower() for k in keyword_titles), reverse=True)
        data["designation"] = ranked[0]  # Use best match
        del data["designations"]  # Clean up


    return data
