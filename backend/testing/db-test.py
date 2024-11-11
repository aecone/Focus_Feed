# test_connection.py
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.config import get_db_connection

conn = get_db_connection()
if conn:
    print("Connection successful!")
    conn.close()
else:
    print("Failed to connect to the database.")
