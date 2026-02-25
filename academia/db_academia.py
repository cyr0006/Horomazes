import sqlite3

DB_PATH = "academia/academia.db"

# Connect to the database
def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS units (
            id INTEGER PRIMARY KEY,
            year INTEGER,
            semester TEXT,
            code TEXT NOT NULL,
            name TEXT NOT NULL,
            score INTEGER,
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

    units = c.execute(
        "SELECT year, semester, code, name, score, grade, notes FROM units ORDER BY year, semester"
    ).fetchall()

    conn.close()

    context = "## CONTEXT\n\n"
    context += "### Units\n"
    context += "\n".join([
        f"- [{u[0]} {u[1]}] {u[2]} — {u[3]} | Score: {u[4]} | Grade: {u[5]}{f' | {u[6]}' if u[6] else ''}"
        for u in units
    ]) or "None logged yet."

    return context

# --- Helpers --- #


def log_unit(code, name, year, semester, score=None, grade=None, notes=None):
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
        INSERT INTO units (year, semester, code, name, score, grade, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (year, semester, code, name, score, grade, notes))

    conn.commit()
    conn.close()