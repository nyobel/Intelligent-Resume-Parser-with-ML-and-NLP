from dotenv import load_dotenv
import os
import pyodbc
import logging

load_dotenv()

# Setup logging
logging.basicConfig(
    filename='insert_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def insert_candidate_data(data):
    """
    Inserts structured candidate data into SQL Server with error handling and logging.
    """
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            f"{os.getenv('DB_EXTRA')};"
            )
        cursor = conn.cursor()

        # Check for duplicate by full_name and email
        cursor.execute("""
            SELECT c.candidate_id
            FROM candidates c
            JOIN contact_info ci ON c.candidate_id = ci.candidate_id
            WHERE c.full_name = ? AND ci.email = ?
        """, data["full_name"], data["email"])

        existing = cursor.fetchone()
        if existing:
            print(f"Candidate '{data['full_name']}' already exists — skipping.")
            logging.info(f"Duplicate skipped: {data['full_name']}")
            return  # Exit early if duplicate found

        # Insert into candidates
        cursor.execute("""
            INSERT INTO candidates (full_name, summary, current_title, location)
            VALUES (?, ?, ?, ?)
        """, data["full_name"], "", data["designation"], "")
        conn.commit()

        candidate_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchval()

        # Insert contact info
        cursor.execute("""
            INSERT INTO contact_info (candidate_id, email, phone, linkedin)
            VALUES (?, ?, ?, ?)
        """, candidate_id, data["email"], data["phone"], "")

        # Insert skills
        for skill in data["skills"]:
            cursor.execute("""
                INSERT INTO skills (candidate_id, skill_name)
                VALUES (?, ?)
            """, candidate_id, skill)

        # Insert education
        if data["education"] or data["institution"]:
            cursor.execute("""
                INSERT INTO education (candidate_id, degree, institution, start_date, end_date)
                VALUES (?, ?, ?, NULL, NULL)
            """, candidate_id, data["education"], data["institution"])

        # Insert experience/project
        if data["project"]:
            cursor.execute("""
                INSERT INTO experiences (candidate_id, job_title, company_name, start_date, end_date, description)
                VALUES (?, ?, ?, NULL, NULL, ?)
            """, candidate_id, data["designation"], "", data["project"])

        conn.commit()
        conn.close()

        success_msg = f"✅ Candidate '{data['full_name']}' inserted successfully."
        print(success_msg)
        logging.info(success_msg)

    except KeyError as e:
        logging.error(f"KeyError - Missing field: {e}")
        print(f"❌ KeyError: {e}")

    except pyodbc.Error as e:
        logging.error(f"Database error: {e}")
        print(f"❌ Database error: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"❌ Unexpected error: {e}")