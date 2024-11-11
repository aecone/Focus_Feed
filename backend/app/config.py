import os
from dotenv import load_dotenv
import psycopg

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '../local.env'))

# Function to connect to the database
def get_db_connection():
    DB_CONFIG = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME")
    }
    try:
        conn = psycopg.connect(**DB_CONFIG)
        print("Connection successful")
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None  


# Test the connection
conn = get_db_connection()
if conn:
    # Close the connection if successful
    conn.close()
