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

events2 = [
    (
        "2025-06-01",
        "project",
        "Built personal website with integrated AI chatbot capable of answering questions about me",
        "Demonstrates full-stack development, AI integration, and personal branding as a developer"
    ),
    (
        "2025-07-01",
        "project",
        "Built a feature-rich daily goals tracking bot for personal use and friend group",
        "Demonstrates bot architecture, multi-user system design, and real-world deployment for ongoing daily use"
    ),
    (
        "2026-01-01",
        "project",
        "Built and configured a personal NAS server using a Raspberry Pi — hosts the goals bot and provides remote file access",
        "Demonstrates hands-on Linux sysadmin, self-hosting, networking, and hardware configuration skills"
    ),
    (
        "2026-02-01",
        "project",
        "Currently building a suite of personal AI agents (finance, academic, fitness, career) with a coordinator architecture — ongoing",
        "Demonstrates agentic AI systems design, Python development, and applied LLM integration in a real personal context"
    ),
]

def seed3():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    inserted = 0
    for date, type_, description, impact in events2:
        existing = c.execute(
            "SELECT id FROM career_events WHERE date = ? AND description = ?",
            (date, description)
        ).fetchone()
        if existing:
            print(f"  SKIP (already exists): {description[:55]}...")
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


jobs = [
    ("Breen Printing",          "Web-to-Print Workflow Developer",                          "2026-02-19", "applied",   "Healesville VIC"),
    ("Future Events Lab",       "Fully Remote - Part Time Analyst / Developer",             "2026-02-17", "applied",   "Carlton VIC — Remote"),
    ("Ottica AI",               "Technical Support & Hardware Technician",                  "2026-02-17", "applied",   "Brunswick East VIC — $30-45/hr"),
    ("Private Advertiser",      "IT Support Technician (Part-Time)",                        "2026-02-19", "rejected",  "Chadstone VIC — expired"),
    ("Valui Healthcare",        "Developer & AI Branding",                                  "2026-02-12", "applied",   "Dandenong South VIC — $33-48/hr, viewed by employer"),
    ("Moose Toys",              "Moose Intern Program",                                     "2026-02-11", "withdrawn", "Melbourne VIC — visited employer site, expired"),
    ("Eastern Health",          "Data Engineer - Research",                                 "2026-02-07", "withdrawn", "Box Hill VIC — visited employer site, expired"),
    ("Tiny Technologies",       "Intern QA Engineer",                                       "2026-02-07", "applied",   "Brisbane QLD — expired"),
    ("Peoplebank Australia",    "Data Analyst (PowerBI/Snowflake/Alteryx/Matillion)",       "2026-01-23", "withdrawn", "Dandenong VIC — $45-55/hr, visited employer site, expired"),
    ("Vanguard Group Pty Ltd",  "Junior Application Engineer",                              "2026-01-22", "withdrawn", "Melbourne VIC — visited employer site, expired"),
    ("NewChurchTek Pty Ltd",    "Casual Software Systems Support",                          "2026-01-22", "applied",   "Melbourne VIC — $29-32/hr, expired"),
    ("PANDA",                   "Data Systems Administrator (Data & Solutions) - Remote",   "2025-12-17", "applied",   "Melbourne VIC — remote, expired"),
    ("Nova Systems Pty Ltd",    "Expressions of Interest - 2027 Graduate Opportunities",   "2025-12-14", "applied",   "Melbourne VIC — visited employer site, expired"),
    ("Hordern Consulting",      "SQL Developer",                                            "2025-12-07", "rejected",  "Melbourne VIC —  expired"),
    ("QEC",                     "Business Intelligence Analyst",                            "2025-11-25", "applied",   "Noble Park VIC — visited employer site"),
]

def seed4():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Add notes column if it doesn't exist
    try:
        c.execute("ALTER TABLE jobs ADD COLUMN notes TEXT")
    except:
        pass

    inserted = 0
    for company, role, date, status, notes in jobs:
        existing = c.execute(
            "SELECT id FROM jobs WHERE company = ? AND role = ?",
            (company, role)
        ).fetchone()
        if existing:
            print(f"  SKIP (already exists): {company} — {role}")
            continue
        c.execute(
            "INSERT INTO jobs (company, role, date_applied, status, notes) VALUES (?, ?, ?, ?, ?)",
            (company, role, date, status, notes)
        )
        print(f"  OK: [{date}] {company} — {role} ({status})")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone. {inserted} jobs inserted.")

if __name__ == "__main__":
    seed()
    seed2() 
    seed3()
    seed4()