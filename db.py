import sqlite3
from datetime import datetime

DB_PATH = "data/career.db"

# Connect to the database
def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            proficiency TEXT,  -- beginner/intermediate/advanced/expert
            last_used DATE,
            notes TEXT
        );

        CREATE TABLE IF NOT EXISTS career_events (
            id INTEGER PRIMARY KEY,
            date DATE NOT NULL,
            type TEXT,  -- achievement/feedback/project/promotion/other
            description TEXT NOT NULL,
            impact TEXT
        );

        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY,
            goal TEXT NOT NULL,
            target_date DATE,
            status TEXT DEFAULT 'active',  -- active/achieved/dropped
            notes TEXT
        );

        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied DATE,
            status TEXT DEFAULT 'applied',  -- applied/screening/interview/offer/rejected/withdrawn
            notes TEXT
        );
    """)
    conn.commit()
    conn.close()

def get_context_block():
    """Pull relevant data to inject into every LLM call"""

    conn = get_conn()
    c = conn.cursor()

    skills = c.execute("SELECT name, proficiency, last_used, notes FROM skills ORDER BY last_used DESC").fetchall()
    events = c.execute("SELECT date, type, description, impact FROM career_events ORDER BY date DESC LIMIT 10").fetchall()
    goals = c.execute("SELECT goal, target_date, status, notes FROM goals WHERE status = 'active'").fetchall()
    jobs = c.execute("SELECT company, role, date_applied, status FROM jobs ORDER BY date_applied DESC LIMIT 10").fetchall()
    
    conn.close()

    context = "## CONTEXT\n\n"

    context += "### Skills\n"
    context += "\n".join([f"- {s[0]} ({s[1]}) — last used: {s[2]} {f'| {s[3]}' if s[3] else ''}" for s in skills]) or "None logged yet."
    
    context += "\n\n### Active Goals\n"
    context += "\n".join([f"- {g[0]} (target: {g[1]}) {f'| {g[3]}' if g[3] else ''}" for g in goals]) or "None logged yet."
    
    context += "\n\n### Recent Career Events\n"
    context += "\n".join([f"- [{e[0]}] {e[1]}: {e[2]} {f'→ {e[3]}' if e[3] else ''}" for e in events]) or "None logged yet."
    
    context += "\n\n### Recent Job Applications\n"
    context += "\n".join([f"- {j[0]} | {j[1]} | applied: {j[2]} | status: {j[3]}" for j in jobs]) or "None logged yet."
    
    return context

# --- Helpers --- #


def log_skill(name, proficiency, last_used=None, notes=None):
    conn = get_conn()
    conn.execute("INSERT INTO skills (name, proficiency, last_used, notes) VALUES (?, ?, ?, ?)",
                 (name, proficiency, last_used or datetime.today().date(), notes))
    conn.commit()
    conn.close()

def log_event(description, type="other", impact=None, date=None):
    conn = get_conn()
    conn.execute("INSERT INTO career_events (date, type, description, impact) VALUES (?, ?, ?, ?)",
                 (date or datetime.today().date(), type, description, impact))
    conn.commit()
    conn.close()

def log_goal(goal, target_date=None, notes=None):
    conn = get_conn()
    conn.execute("INSERT INTO goals (goal, target_date, notes) VALUES (?, ?, ?)",
                 (goal, target_date, notes))
    conn.commit()
    conn.close()

def log_job(company, role, date_applied=None, notes=None):
    conn = get_conn()
    conn.execute("INSERT INTO jobs (company, role, date_applied, notes) VALUES (?, ?, ?, ?)",
                 (company, role, date_applied or datetime.today().date(), notes))
    conn.commit()
    conn.close()