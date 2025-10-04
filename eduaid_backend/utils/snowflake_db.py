from dotenv import load_dotenv
import os
import snowflake.connector

# Load your api.env
load_dotenv("api.env")

SNOW_USER = os.getenv("SNOWFLAKE_USER")
SNOW_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOW_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOW_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOW_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOW_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")


def get_connection():
    """Create and return a Snowflake Connection."""
    return snowflake.connector.connect(
        user=SNOW_USER,
        password=SNOW_PASSWORD,
        account=SNOW_ACCOUNT,
        warehouse=SNOW_WAREHOUSE,
        database=SNOW_DATABASE,
        schema=SNOW_SCHEMA,
        autocommit=True,
    )


def test_connection():
    """Test the Snowflake connection and print current context."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT CURRENT_USER(), CURRENT_DATABASE(), CURRENT_SCHEMA()")
        result = cur.fetchone()
        print("✅ Connected successfully! Info:", result)
    except Exception as e:
        print("❌ Connection failed:", e)
    finally:
        if conn:
            conn.close()


def save_to_db(data: dict) -> bool:
    """
    Save a summary record to the database.
    `data` should have keys `"input"` and `"summary"`.
    """
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Use parameter binding to avoid SQL injection
        cur.execute(
            "INSERT INTO summaries (input_text, summary_text) VALUES (%s, %s)",
            (data["input"], data["summary"]),
        )
        cur.close()
        return True
    except Exception as e:
        print("Snowflake save_to_db error:", e)
        return False
    finally:
        if conn:
            conn.close()


def fetch_history(limit: int = 10):
    """
    Return the most recent `limit` summaries.
    Returns a list of dictionaries with keys: input, summary, created_at.
    """
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Adjust column names to match your table definition
        cur.execute(
            f"SELECT input_text, summary_text, created_at FROM summaries "
            f"ORDER BY created_at DESC LIMIT {limit}"
        )
        rows = cur.fetchall()
        result = []
        for row in rows:
            input_text = row[0]
            summary_text = row[1]
            created_at = row[2]
            # Convert timestamp to string if needed
            if hasattr(created_at, "isoformat"):
                created_at = created_at.isoformat()
            result.append(
                {
                    "input": input_text,
                    "summary": summary_text,
                    "created_at": created_at,
                }
            )
        cur.close()
        return result
    except Exception as e:
        print("Snowflake fetch_history error:", e)
        return []
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    test_connection()
