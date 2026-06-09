import sqlite3
from datetime import datetime

DB_PATH = "finance.db"

# Connect to the database
def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.executescript(""" 
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY, 
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            notes TEXT
        );
    """)
    conn.commit()
    conn.close()

def get_context_block():
    """Pull relevant data to inject into every LLM call"""

    
    return None

# --- Helpers --- #
