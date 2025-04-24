import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to the SQL Server
def get_connection():
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"{os.getenv('DB_EXTRA')};"
    )

# Query the candidates and their metadata
def fetch_resume_data():
    query = """
    SELECT 
        c.candidate_id,
        c.full_name,
        c.current_title,
        ci.email,
        ci.phone,
        e.degree,
        e.institution,
        ex.description AS experience,
        s.skill_name
    FROM candidates c
    LEFT JOIN contact_info ci ON c.candidate_id = ci.candidate_id
    LEFT JOIN education e ON c.candidate_id = e.candidate_id
    LEFT JOIN experiences ex ON c.candidate_id = ex.candidate_id
    LEFT JOIN skills s ON c.candidate_id = s.candidate_id
    """
    
    with get_connection() as conn:
        df = pd.read_sql(query, conn)

    return df

# Fetch and transform data for ML
raw_df = fetch_resume_data()

# Group skills by candidate
agg_df = (raw_df.groupby(
    ['candidate_id', 'full_name', 'current_title', 'email', 'phone', 'degree', 'institution', 'experience'])
    .agg({'skill_name': lambda x: list(filter(None, set(x)))})
    .reset_index()
)

# Show cleaned dataset
print(agg_df.head())