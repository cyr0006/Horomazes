import sqlite3
from datetime import datetime

DB_PATH = "data/career.db"

skills = [
    # Programming Languages
    ("Python",              "intermediate",      "programming"),
    ("JavaScript",          "intermediate",      "programming"),
    ("Java",                "beginner",  "programming"),
    ("MATLAB",              "beginner",  "programming"),
    ("SQL",                 "intermediate",      "programming"),
    ("NoSQL",               "intermediate",      "programming"),
    ("Assembly",            "beginner",      "programming"),
    ("C++",                 "beginner",  "programming"),

    # Markup / Web
    ("HTML",                "intermediate",      "web"),
    ("CSS",                 "intermediate",      "web"),
    ("Shell Scripting",     "intermediate",  "devops"),
    ("React",               "intermediate",      "web"),
    ("Tailwind",            "beginner",      "web"),
    ("Vite",                "intermediate",  "web"),

    # CS Fundamentals
    ("Data Structures & Algorithms", "intermediate", "cs_fundamentals"),
    ("Discrete Mathematics",         "advanced", "cs_fundamentals"),

    # Databases
    ("MongoDB",             "intermediate",      "databases"),
    ("Cassandra",           "intermediate",  "databases"),
    ("Neo4j",               "intermediate",  "databases"),

    # DevOps & Tools
    ("Git",                 "intermediate",      "devops"),
    ("Docker",              "intermediate",      "devops"),
    ("CI/CD",               "intermediate",  "devops"),
    ("Software Testing",    "intermediate",  "devops"),
    ("Security Testing",    "intermediate",  "devops"),
    ("VMware",              "intermediate",  "devops"),
    ("Ubuntu Linux",        "intermediate",      "devops"),

    # Data & BI
    ("Microsoft Office",    "advanced",      "data_bi"),
    ("Power BI",            "intermediate",  "data_bi"),
    ("Data Warehousing",    "intermediate",  "data_bi"),
    ("Data Cleaning",       "intermediate",  "data_bi"),
    ("OLAP",                "intermediate",  "data_bi"),

    # Other
    ("CRM Systems",         "advanced",  "enterprise"),
    ("Accounting Software", "intermediate",  "enterprise"),
    ("SolidWorks",          "intermediate",      "cad"),
    ("Fusion360",           "intermediate",      "cad"),
]

def seed():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Add category column if it doesn't exist yet
    try:
        c.execute("ALTER TABLE skills ADD COLUMN category TEXT")
    except sqlite3.OperationalError:
        pass  # column already exists

    today = datetime.today().date()
    inserted = 0

    for name, proficiency, category in skills:
        existing = c.execute("SELECT id FROM skills WHERE name = ?", (name,)).fetchone()
        if existing:
            print(f"  SKIP (already exists): {name}")
            continue
        c.execute(
            "INSERT INTO skills (name, proficiency, last_used, category) VALUES (?, ?, ?, ?)",
            (name, proficiency, today, category)
        )
        print(f"  OK: {name} ({proficiency}) [{category}]")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone. {inserted} skills inserted.")

events = [
    ("2022-02-01", "education",    "Enrolled in Bachelor of Software Engineering at Monash University (4 year course)", None),
    ("2022-06-01", "setback",      "Began struggling academically — over 2022-2024 failed approximately 6 units, falling 2 years behind schedule", "Significant mental health impact; long-term consequences still felt today"),
    ("2023-03-01", "employment",   "Started working at Cardinia Shire Council as a Customer Support Officer", "Casual role at $41/hr — provided financial stability during difficult academic period"),
    ("2025-01-01", "achievement",  "Began academic recovery — improved grades, built better habits, raised average to a Distinction", "Turning point; marks a significant personal and academic turnaround"),
    ("2026-01-01", "education",    "Approximately 2 years remaining in degree as of early 2026", "Most core units complete; remaining time driven by 2 year-long units. 2027 expected to be light (2 units per semester)"),
]

def seed2():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    inserted = 0
    for date, type_, description, impact in events:
        existing = c.execute("SELECT id FROM career_events WHERE date = ? AND description = ?", (date, description)).fetchone()
        if existing:
            print(f"  SKIP (already exists): {description[:50]}...")
            continue
        c.execute(
            "INSERT INTO career_events (date, type, description, impact) VALUES (?, ?, ?, ?)",
            (date, type_, description, impact)
        )
        print(f"  OK: [{date}] {description[:60]}...")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone. {inserted} events inserted.")


if __name__ == "__main__":
    seed()
    seed2()