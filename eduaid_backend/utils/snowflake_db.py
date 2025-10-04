from dotenv import load_dotenv
import os
import snowflake.connector

# Load your api.env (make sure path is correct)
load_dotenv("api.env")

SNOW_USER = os.getenv("SNOWFLAKE_USER")
SNOW_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOW_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOW_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOW_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOW_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")


def get_connection():
    """Create and return a live Snowflake connection."""
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
    """Test Snowflake connection and print info."""
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


if __name__ == "__main__":
    test_connection()
