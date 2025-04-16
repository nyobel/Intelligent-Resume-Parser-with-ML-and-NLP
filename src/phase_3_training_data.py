"""
Step 2: Training Data for Custom NER (Phase 3)

This file contains manually annotated training data
for training a custom spaCy NER model.

Labels: NAME, EMAIL, PHONE, EDUCATION, SKILLS, EXPERIENCE, DESIGNATION, PROJECT

Each entry includes a sentence and the labeled entities it contains.
"""

TRAINING_DATA = [
    # 1. EXPERIENCE
    (
        "Set up and managed the risk framework, lead customer audits, assisted in new customer proposals to leading banks.",
        {"entities": [(0, 140, "EXPERIENCE")]}
    ),

    # 2. NAME, PHONE, EMAIL
    (
        "Name: Lee Li Ting | Contact: 9876 1091 | Email: ltlee74@gmail.com",
        {"entities": [(6, 18, "NAME"), (30, 39, "PHONE"), (48, 66, "EMAIL")]}
    ),

    # 3. DESIGNATION, EXPERIENCE
    (
        "Director, Finance at EDBI Pte Ltd (2015 - Present)",
        {"entities": [(0, 17, "DESIGNATION"), (21, 46, "EXPERIENCE")]}
    ),

    # 4. EDUCATION
    (
        "Bachelor of Accountancy 1996 - Nanyang Technological University",
        {"entities": [(0, 66, "EDUCATION")]}
    ),

    # 5. EDUCATION
    (
        "Institute of Chartered Accountants of India - Associate Member",
        {"entities": [(0, 59, "EDUCATION")]}
    ),

    # 6. DESIGNATION, EXPERIENCE
    (
        "Head of Risk & Compliance at Copal Amba (Jan 2010 – Oct 2010)",
        {"entities": [(0, 27, "DESIGNATION"), (31, 60, "EXPERIENCE")]}
    ),

    # 7. SKILLS
    (
        "Proficient in Microsoft Office Suite, JDE One World, Quickbooks, IBM S36",
        {"entities": [(16, 42, "SKILLS"), (44, 58, "SKILLS"), (60, 70, "SKILLS"), (72, 79, "SKILLS")]}
    ),

    # 8. PROJECT
    (
        "Built a real estate close ended fund with assets located in Thailand, Korea, Singapore and Malaysia.",
        {"entities": [(0, 92, "PROJECT")]}
    ),

    # 9. DESIGNATION
    (
        "Vice President, Xander Group",
        {"entities": [(0, 14, "DESIGNATION")]}
    ),

    # 10. EXPERIENCE
    (
        "Successfully prepared due diligence documents for fund raising and met prospective investors.",
        {"entities": [(0, 94, "EXPERIENCE")]}
    ),

    # 11. SKILLS
    (
        "She is proficient in Python, Django, and JavaScript.",
        {"entities": [(23, 29, "SKILLS"), (31, 37, "SKILLS"), (43, 53, "SKILLS")]}
    ),

    # 12. NAME, PROJECT, SKILLS
    (
        "Kevin Odhiambo developed an e-commerce platform using Flask.",
        {"entities": [(0, 15, "NAME"), (26, 47, "PROJECT"), (55, 60, "SKILLS")]}
    ),

    # 13. NAME, DESIGNATION, EXPERIENCE
    (
        "Miriam Koech served as a Data Scientist at Microsoft.",
        {"entities": [(0, 13, "NAME"), (25, 39, "DESIGNATION"), (43, 52, "EXPERIENCE")]}
    ),

    # 14. NAME
    (
        "Her full name is Alice Johnson.",
        {"entities": [(18, 31, "NAME")]}
    ),

    # 15. EDUCATION
    (
        "She holds a BSc in Computer Science from Kenyatta University.",
        {"entities": [(14, 46, "EDUCATION")]}
    ),

    # 16. EDUCATION
    (
        "Completed a Master of Science in Artificial Intelligence at UoN in 2021.",
        {"entities": [(11, 53, "EDUCATION")]}  # 'Master of Science in Artificial Intelligence'
    ),
    # 17. NAME
    ("Name: Brian Otieno", {"entities": [(6, 19, "NAME")]}),

    # 18. NAME
    ("Full name: Sarah Wanjiku", {"entities": [(11, 24, "NAME")]}),

    # 19. EMAIL
    ("Reach me at: sarah.w@example.com", {"entities": [(13, 34, "EMAIL")]}),

    # 20. PHONE
    ("Contact: +254712345678", {"entities": [(9, 22, "PHONE")]}),

    # 21. EDUCATION
    ("Holds a BSc in Information Technology from JKUAT.", {"entities": [(10, 45, "EDUCATION")]}),

    # 22. EDUCATION
    ("Graduated with a Master’s in Data Science from Strathmore University.", {"entities": [(18, 57, "EDUCATION")]}),

    # 23. SKILLS
    ("Skilled in HTML, CSS, JavaScript, and Git.", {"entities": [(12, 16, "SKILLS"), (18, 21, "SKILLS"), (23, 33, "SKILLS"), (39, 42, "SKILLS")]}),

    # 24. SKILLS
    ("Python, Django, Flask, and PostgreSQL", {"entities": [(0, 6, "SKILLS"), (8, 14, "SKILLS"), (16, 21, "SKILLS"), (28, 39, "SKILLS")]}),

    # 25. DESIGNATION
    ("Worked as a Backend Developer at Cellulant.", {"entities": [(13, 30, "DESIGNATION"), (34, 43, "EXPERIENCE")]}),

    # 26. EXPERIENCE
    ("Led deployment for cross-border payments platform.", {"entities": [(0, 52, "EXPERIENCE")]}),

    # 27. PROJECT
    ("Built a hotel booking app using React Native.", {"entities": [(0, 36, "PROJECT"), (43, 55, "SKILLS")]}),

    # 28. PROJECT
    ("Created a document parser that extracts skills from resumes.", {"entities": [(0, 57, "PROJECT")]}),

    # 29. EXPERIENCE
    ("Managed a team of 5 engineers across 3 continents.", {"entities": [(0, 49, "EXPERIENCE")]}),

    # 30. NAME, DESIGNATION
    ("Lucy Mwende is a Senior Data Analyst at Safaricom.", {"entities": [(0, 11, "NAME"),  (18, 37, "DESIGNATION"), (41, 51, "EXPERIENCE")]}),

     # 31. DESIGNATION
    ("She worked as a Software Engineer at Andela.", {"entities": [(17, 34, "DESIGNATION")] }),

    # 32. SKILLS
    ("He is proficient in JavaScript and React.", {"entities": [(21, 31, "SKILLS"), (36, 42, "SKILLS")]}),

    # 33. SKILLS
    ("Her technical stack includes Django, PostgreSQL, and Docker.", {"entities": [(29, 35, "SKILLS"), (37, 48, "SKILLS"), (54, 60, "SKILLS")]}),

    # 34. DESIGNATION
    ("Appointed as Senior Backend Engineer at Twiga Foods.", {"entities": [(14, 38, "DESIGNATION"), (42, 54, "EXPERIENCE")]}),

    # 35. SKILLS
    ("Worked with TensorFlow, Pandas, and NumPy on a data science project.", {"entities": [(12, 22, "SKILLS"), (24, 30, "SKILLS"), (36, 41, "SKILLS")]}),

    # 36. NAME
    ("Name: Prakash Patel", {"entities": [(6, 20, "NAME")]}),

    # 37. NAME
    ("Full name: Catherine Njoki", {"entities": [(11, 27, "NAME")]}),

    # 38. NAME
    ("Candidate: David Njoroge", {"entities": [(11, 26, "NAME")]}),

    # 39. DESIGNATION
    ("Worked as Marketing Lead at a regional bank.", {"entities": [(11, 25, "DESIGNATION")]}),

    # 40. DESIGNATION
    ("Appointed as Finance Director for East Africa.", {"entities": [(14, 31, "DESIGNATION")]}),

    # 41. DESIGNATION
    ("Held the role of Assistant Manager.", {"entities": [(18, 35, "DESIGNATION")]}),

    # 42. SKILLS
    ("Proficient in SEO, SEM, and Google Analytics.", {"entities": [(16, 19, "SKILLS"), (21, 24, "SKILLS"), (30, 47, "SKILLS")]}),

    # 43. SKILLS
    ("Technologies used: Docker, Kubernetes, Jenkins.", {"entities": [(20, 26, "SKILLS"), (28, 38, "SKILLS"), (40, 47, "SKILLS")]}),

    # 44. SKILLS
    ("Familiar with MySQL, MongoDB, and Redis.", {"entities": [(15, 20, "SKILLS"), (22, 29, "SKILLS"), (35, 40, "SKILLS")]}),

    # 45. SKILLS
    ("Experienced in Tableau, Power BI, and Excel.", {"entities": [(18, 25, "SKILLS"), (27, 35, "SKILLS"), (41, 46, "SKILLS")]}),

    # 46. EDUCATION
    ("Bachelor of Science in Computer Science from Daystar University.", {"entities": [(0, 53, "EDUCATION")]}),

    # 47. EDUCATION
    ("Earned a degree in Finance from Strathmore University.", {"entities": [(17, 48, "EDUCATION")]}),

    # 48. EDUCATION
    ("Graduated with a Diploma in Software Development at Moringa School.", {"entities": [(18, 55, "EDUCATION")]}),

    # 49. PHONE clarification
    ("Mobile: 0700123456", {"entities": [(8, 18, "PHONE")]}),

    # 50. PHONE clarification
    ("Phone Number: +254-701-123456", {"entities": [(14, 28, "PHONE")]}),

    # 51. EMAIL
    ("Email: brian.o@example.com", {"entities": [(7, 27, "EMAIL")]}),

    # 52. EMAIL
    ("Reach me at j.kimani@company.org for details.", {"entities": [(12, 33, "EMAIL")]}),

    # 53. EMAIL
    ("Contact: dorothy.w@firm.co.ke", {"entities": [(9, 30, "EMAIL")]}),

    # 54. NAME
    ("Candidate Name: Brian Otieno", {"entities": [(16, 29, "NAME")]}),

    # 55. NAME
    ("Full name: Miriam Achieng", {"entities": [(11, 26, "NAME")]}),

    # 56. EDUCATION
    ("Bachelor of Commerce in Finance from Nairobi University.", {"entities": [(0, 50, "EDUCATION")]}),

    # 57. EDUCATION
    ("Diploma in Human Resource Management from Zetech College.", {"entities": [(0, 53, "EDUCATION")]}),

    # 58. DESIGNATION
    ("Position held: Senior HR Consultant", {"entities": [(16, 36, "DESIGNATION")]}),

    # 59. DESIGNATION
    ("Role: Procurement Officer at ABC Ltd.", {"entities": [(6, 26, "DESIGNATION")]}),

    # 60. EXPERIENCE
    ("Handled payroll, tax reconciliation, and statutory reporting.", {"entities": [(0, 61, "EXPERIENCE")]}),

    # 61. EMAIL
    ("Primary email: alice.njoroge@company.com", {"entities": [(15, 41, "EMAIL")]}),

    # 62. EMAIL
    ("Reach me via: mark.okello@devhub.io", {"entities": [(14, 37, "EMAIL")]}),

    # 63. EMAIL
    ("Contact address: felix.mutiso@cloud.africa", {"entities": [(17, 47, "EMAIL")]}),

    # 64. EMAIL
    ("Work Email - james.kariuki@enterprise.co.ke", {"entities": [(13, 47, "EMAIL")]}),

    # 65. EMAIL
    ("Email ID: ruth.maina@financegroup.org", {"entities": [(10, 42, "EMAIL")]}),

    # 66. EDUCATION
    ("Bachelor of Science in Software Engineering from Kenyatta University", {"entities": [(0, 61, "EDUCATION")]}),

    # 67. EDUCATION
    ("Earned a BA in Economics at University of Nairobi", {"entities": [(10, 47, "EDUCATION")]}),

    # 68. EDUCATION
    ("Diploma in Supply Chain Management from Kenya Institute of Management", {"entities": [(0, 61, "EDUCATION")]}),

    # 69. EDUCATION
    ("Master’s in Artificial Intelligence from Strathmore University", {"entities": [(0, 54, "EDUCATION")]}),

    # 70. EDUCATION
    ("Completed a Certificate in Data Analytics from Moringa School", {"entities": [(11, 58, "EDUCATION")]})
]

