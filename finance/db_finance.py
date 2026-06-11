import sqlite3
from datetime import datetime

DB_PATH = "finance/finance.db"
# Connect to the database
def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.executescript(""" 
        CREATE TABLE IF NOT EXISTS MONTHLY_COSTS (
            id INTEGER PRIMARY KEY, 
            month TEXT NOT NULL,
            amount REAL NOT NULL,
            notes TEXT
        );
    """)
    conn.commit()
    conn.close()

def get_context_block():
    """Pull relevant data to inject into every LLM call"""

    
    return None

def log_monthly_cost(month, amount, notes=None):
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        "INSERT INTO MONTHLY_COSTS (month, amount, notes) VALUES (?, ?, ?)",
        (month, amount, notes)
    )
    conn.commit()
    conn.close()

# --- Helpers --- #
