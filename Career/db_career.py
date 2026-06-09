import sqlite3
from datetime import datetime

DB_PATH = "career/career.db"


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied DATE,
            status TEXT DEFAULT 'applied',
            notes TEXT
        );
    """)
    conn.commit()
    conn.close()


def get_context_block():
    conn = get_conn()
    c = conn.cursor()
    jobs = c.execute(
        "SELECT company, role, date_applied, status, notes FROM jobs ORDER BY date_applied DESC"
    ).fetchall()
    conn.close()

    if not jobs:
        return "### Job Applications\nNone logged yet."

    lines = [
        f"- {j[0]} | {j[1]} | applied: {j[2]} | status: {j[3]}{f' | {j[4]}' if j[4] else ''}"
        for j in jobs
    ]
    return "### Job Applications\n" + "\n".join(lines)


def log_job(company, role, date_applied=None, notes=None):
    conn = get_conn()
    conn.execute(
        "INSERT INTO jobs (company, role, date_applied, notes) VALUES (?, ?, ?, ?)",
        (company, role, date_applied or datetime.today().date(), notes)
    )
    conn.commit()
    conn.close()


def update_job(job_id, status=None, notes=None):
    conn = get_conn()
    if status:
        conn.execute("UPDATE jobs SET status = ? WHERE id = ?", (status, job_id))
    if notes:
        conn.execute("UPDATE jobs SET notes = ? WHERE id = ?", (notes, job_id))
    conn.commit()
    conn.close()