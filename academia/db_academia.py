import sqlite3
from datetime import datetime

DB_PATH = "academia.db"

# Connect to the database
def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS units (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            enrolment_period TEXT,  -- Sem x YYYY
            grade TEXT,
            notes TEXT
        );

    """)
    conn.commit()
    conn.close()

def get_context_block():
    """Pull relevant data to inject into every LLM call"""

    conn = get_conn()
    c = conn.cursor()

    units = c.execute("SELECT name, enrolment_period, grade, notes FROM units ORDER BY enrolment_period DESC").fetchall()    
    conn.close()

    context = "## CONTEXT\n\n"

    context += "### Units\n"
    context += "\n".join([f"- {u[0]} ({u[1]}) — grade: {u[2]} {f'| {u[3]}' if u[3] else ''}" for u in units]) or "None logged yet."
    
    return context

# --- Helpers --- #


def log_unit(name, enrolment_period, grade=None, notes=None):
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
        INSERT INTO units (name, enrolment_period, grade, notes)
        VALUES (?, ?, ?, ?)
    """, (name, enrolment_period, grade, notes))

    conn.commit()
    conn.close()