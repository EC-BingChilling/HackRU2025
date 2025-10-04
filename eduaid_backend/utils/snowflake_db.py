import os
from dotenv import load_dotenv
import snowflake.connector

# Load your credentials (assume they are in api.env)
load_dotenv("api.env")

SNOW_USER = os.getenv("SNOWFLAKE_USER")
SNOW_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOW_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOW_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOW_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOW_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")


def get_connection():
    # You might want to cache connections or use a connection pool in prod
    conn = snowflake.connector.connect(
        user=SNOW_USER,
        password=SNOW_PASSWORD,
        account=SNOW_ACCOUNT,
        warehouse=SNOW_WAREHOUSE,
        database=SNOW_DATABASE,
        schema=SNOW_SCHEMA,
        autocommit=True,
    )
    return conn


def save_to_db(data: dict) -> bool:
    """
    Expect data dict like {"input": "...", "summary": "..."} etc.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Example: assume table eduaid.summaries(input_text, summary_text, created_at)
        sql = """
        INSERT INTO summaries (input_text, summary_text)
        VALUES (%(input)s, %(summary)s)
        """
        cur.execute(sql, data)
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print("Snowflake save error:", e)
        return False


def fetch_history(limit: int = 10):
    """
    Example: return last N saved summaries.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            f"SELECT input_text, summary_text, created_at FROM summaries ORDER BY created_at DESC LIMIT {limit}"
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        # Return list of dicts
        result = [
            {"input": row[0], "summary": row[1], "created_at": row[2]} for row in rows
        ]
        return result
    except Exception as e:
        print("Snowflake fetch error:", e)
        return []
