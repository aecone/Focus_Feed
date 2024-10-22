import os
from dotenv import load_dotenv
import psycopg

# Load environment variables
load_dotenv('local.env')

# Function to connect to the database
def get_db_connection():
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    dbname = os.getenv("POSTGRES_DBNAME")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
    
    try:
        # Attempt connection to the database
        conn = psycopg.connect(conn_string, options='-c idle_in_transaction_session_timeout=500000')
        print("Connection successful")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Test the connection
conn = get_db_connection()
if conn:
    # Close the connection if successful
    conn.close()
