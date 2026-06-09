from random import seed
import sqlite3
from datetime import datetime

DB_PATH = "academia/academia.db"

# skills = [
#     # Programming Languages
#     ("Python",              "intermediate",      "programming"),
#     ("JavaScript",          "intermediate",      "programming"),
#     ("Java",                "beginner",  "programming"),
#     ("MATLAB",              "beginner",  "programming"),
#     ("SQL",                 "intermediate",      "programming"),
#     ("NoSQL",               "intermediate",      "programming"),
#     ("Assembly",            "beginner",      "programming"),
#     ("C++",                 "beginner",  "programming"),

#     # Markup / Web
#     ("HTML",                "intermediate",      "web"),
#     ("CSS",                 "intermediate",      "web"),
#     ("Shell Scripting",     "intermediate",  "devops"),
#     ("React",               "intermediate",      "web"),
#     ("Tailwind",            "beginner",      "web"),
#     ("Vite",                "intermediate",  "web"),

#     # CS Fundamentals
#     ("Data Structures & Algorithms", "intermediate", "cs_fundamentals"),
#     ("Discrete Mathematics",         "advanced", "cs_fundamentals"),

#     # Databases
#     ("MongoDB",             "intermediate",      "databases"),
#     ("Cassandra",           "intermediate",  "databases"),
#     ("Neo4j",               "intermediate",  "databases"),

#     # DevOps & Tools
#     ("Git",                 "intermediate",      "devops"),
#     ("Docker",              "intermediate",      "devops"),
#     ("CI/CD",               "intermediate",  "devops"),
#     ("Software Testing",    "intermediate",  "devops"),
#     ("Security Testing",    "intermediate",  "devops"),
#     ("VMware",              "intermediate",  "devops"),
#     ("Ubuntu Linux",        "intermediate",      "devops"),

#     # Data & BI
#     ("Microsoft Office",    "advanced",      "data_bi"),
#     ("Power BI",            "intermediate",  "data_bi"),
#     ("Data Warehousing",    "intermediate",  "data_bi"),
#     ("Data Cleaning",       "intermediate",  "data_bi"),
#     ("OLAP",                "intermediate",  "data_bi"),

#     # Other
#     ("CRM Systems",         "advanced",  "enterprise"),
#     ("Accounting Software", "intermediate",  "enterprise"),
#     ("SolidWorks",          "intermediate",      "cad"),
#     ("Fusion360",           "intermediate",      "cad"),
# ]

# def seed():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     # Add category column if it doesn't exist yet
#     try:
#         c.execute("ALTER TABLE skills ADD COLUMN category TEXT")
#     except sqlite3.OperationalError:
#         pass  # column already exists

#     today = datetime.today().date()
#     inserted = 0

#     for name, proficiency, category in skills:
#         existing = c.execute("SELECT id FROM skills WHERE name = ?", (name,)).fetchone()
#         if existing:
#             print(f"  SKIP (already exists): {name}")
#             continue
#         c.execute(
#             "INSERT INTO skills (name, proficiency, last_used, category) VALUES (?, ?, ?, ?)",
#             (name, proficiency, today, category)
#         )
#         print(f"  OK: {name} ({proficiency}) [{category}]")
#         inserted += 1

#     conn.commit()
#     conn.close()
#     print(f"\nDone. {inserted} skills inserted.")

# events = [
#     ("2022-02-01", "education",    "Enrolled in Bachelor of Software Engineering at Monash University (4 year course)", None),
#     ("2022-06-01", "setback",      "Began struggling academically — over 2022-2024 failed approximately 6 units, falling 2 years behind schedule", "Significant mental health impact; long-term consequences still felt today"),
#     ("2023-03-01", "employment",   "Started working at Cardinia Shire Council as a Customer Support Officer", "Casual role at $41/hr — provided financial stability during difficult academic period"),
#     ("2025-01-01", "achievement",  "Began academic recovery — improved grades, built better habits, raised average to a Distinction", "Turning point; marks a significant personal and academic turnaround"),
#     ("2026-01-01", "education",    "Approximately 2 years remaining in degree as of early 2026", "Most core units complete; remaining time driven by 2 year-long units. 2027 expected to be light (2 units per semester)"),
# ]

# def seed2():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     inserted = 0
#     for date, type_, description, impact in events:
#         existing = c.execute("SELECT id FROM career_events WHERE date = ? AND description = ?", (date, description)).fetchone()
#         if existing:
#             print(f"  SKIP (already exists): {description[:50]}...")
#             continue
#         c.execute(
#             "INSERT INTO career_events (date, type, description, impact) VALUES (?, ?, ?, ?)",
#             (date, type_, description, impact)
#         )
#         print(f"  OK: [{date}] {description[:60]}...")
#         inserted += 1

#     conn.commit()
#     conn.close()
#     print(f"\nDone. {inserted} events inserted.")

# events2 = [
#     (
#         "2025-06-01",
#         "project",
#         "Built personal website with integrated AI chatbot capable of answering questions about me",
#         "Demonstrates full-stack development, AI integration, and personal branding as a developer"
#     ),
#     (
#         "2025-07-01",
#         "project",
#         "Built a feature-rich daily goals tracking bot for personal use and friend group",
#         "Demonstrates bot architecture, multi-user system design, and real-world deployment for ongoing daily use"
#     ),
#     (
#         "2026-01-01",
#         "project",
#         "Built and configured a personal NAS server using a Raspberry Pi — hosts the goals bot and provides remote file access",
#         "Demonstrates hands-on Linux sysadmin, self-hosting, networking, and hardware configuration skills"
#     ),
#     (
#         "2026-02-01",
#         "project",
#         "Currently building a suite of personal AI agents (finance, academic, fitness, career) with a coordinator architecture — ongoing",
#         "Demonstrates agentic AI systems design, Python development, and applied LLM integration in a real personal context"
#     ),
# ]

# def seed3():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     inserted = 0
#     for date, type_, description, impact in events2:
#         existing = c.execute(
#             "SELECT id FROM career_events WHERE date = ? AND description = ?",
#             (date, description)
#         ).fetchone()
#         if existing:
#             print(f"  SKIP (already exists): {description[:55]}...")
#             continue
#         c.execute(
#             "INSERT INTO career_events (date, type, description, impact) VALUES (?, ?, ?, ?)",
#             (date, type_, description, impact)
#         )
#         print(f"  OK: [{date}] {description[:60]}...")
#         inserted += 1

#     conn.commit()
#     conn.close()
#     print(f"\nDone. {inserted} events inserted.")

DB_PATH = "career/career.db"


jobs = [
    ("KPMG",                   "2026/27 KPMG Vacationer Program - Technology & Digital",     "2026-04-07", "haven't heard back, Likely intakes are later in year",   "location: Melbourne VIC"),
    ("Deloitte",               "Deloitte Cyber Vacationer Program | 2026/27",                "2026-03-06", "haven't heard back, Likely intakes are later in year",   "location: Melbourne VIC"),
    ("Quantium",               "Quantium Data Analytics Virtual Experience Program",         "2026-02-10", "haven't heard back, Likely intakes are later in year",   "location: Melbourne VIC"),
    ("Airwallex",              "2026/27 Software Engineering Intern Program",               "2026-03-06", "haven't heard back, Likely intakes are later in year",   "location: Melbourne VIC"),
    ("SEEK Grad",              "2026/27 EY Vacationer Program - Computer Science",          "2026-03-06", "haven't heard back, Likely intakes are later in year",   "location: Melbourne VIC"),
    ("BHP",                    "BHP 2026 Intern Program",                                   "2026-03-06", "haven't heard back, Likely intakes are later in year",   "location: Melbourne VIC"),
    ("Breen Printing",          "Web-to-Print Workflow Developer",                          "2026-02-19", "Never responded ",   "location: Healesville VIC"),
    ("Future Events Lab",       "Fully Remote - Part Time Analyst / Developer",             "2026-02-17", "Never responded",   "location: Carlton VIC — Remote"),
    ("Ottica AI",               "Technical Support & Hardware Technician",                  "2026-02-17", "Never responded ",   "location: Brunswick East VIC"),
    ("Private Advertiser",      "IT Support Technician (Part-Time)",                        "2026-02-19", "Never responded ",  "location: Chadstone VIC"),
    ("Valui Healthcare",        "Developer & AI Branding",                                  "2026-02-12", "Never responded ",   "location: Dandenong South VIC "),
    ("Moose Toys",              "Moose Intern Program",                                     "2026-02-11", "Never responded ", "location: Melbourne VIC"),
    ("Eastern Health",          "Data Engineer - Research",                                 "2026-02-07", "Never responded ", "location: Box Hill VIC "),
    ("Tiny Technologies",       "Intern QA Engineer",                                       "2026-02-07", "Never responded ",   "location: Brisbane QLD"),
    ("Peoplebank Australia",    "Data Analyst (PowerBI/Snowflake/Alteryx/Matillion)",       "2026-01-23", "Never responded ", "location: Dandenong VIC"),
    ("Vanguard Group Pty Ltd",  "Junior Application Engineer",                              "2026-01-22", "Never responded ", "location: Melbourne VIC"),
    ("NewChurchTek Pty Ltd",    "Casual Software Systems Support",                          "2026-01-22", "Never responded ",   "location: Melbourne VIC"),
    ("PANDA",                   "Data Systems Administrator (Data & Solutions) - Remote",   "2025-12-17", "Rejected ",   "location: Melbourne VIC"),
    ("Nova Systems Pty Ltd",    "Expressions of Interest - 2027 Graduate Opportunities",   "2025-12-14", "rejected ",   "location: Melbourne VIC"),
    ("Hordern Consulting",      "SQL Developer",                                            "2025-12-07", "Never responded ",  "location: Melbourne VIC"),
    ("QEC",                     "Business Intelligence Analyst",                            "2025-11-25", "Never responded ",   "location: Noble Park VIC"),
]

def seed_applications():
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

# units = [
#     (2022,"Sem1", "ENG1011", "ENGINEERING METHODS", 55, "P"),
#     (2022,"Sem1", "ENG1012", "ENGINEERING DESIGN", 76, "D"),
#     (2022,"Sem1", "ENG1013", "ENGINEERING SMART SYSTEMS",  72, "D"),
#     (2022,"Sem1", "ENG1090", "FOUNDATION MATHEMATICS",  62, "C"),
#     (2022,"Sem2", "ENG1005", "ENGINEERING MATHEMATICS", 17, "N"),
#     (2022,"Sem2", "ENG1014", "ENGINEERING NUMERICAL ANALYSIS", 42, "N"),
#     (2022,"Sem2", "FIT1056", "COLLABORATIVE ENGINEERING FOR WEB APPLICATIONS", 83, "HD"),
#     (2022,"Sem2", "PHS1002", "PHYSICS FOR ENGINEERING", 42, "N"),
#     (2023,"Sem1", "ENG1005", "ENGINEERING MATHEMATICS",  None, "DISCONTINUED"),
#     (2023,"Sem1", "ENG1014", "ENGINEERING NUMERICAL ANALYSIS",  57, "P"),
#     (2023,"Sem1", "FIT1045", "INTRODUCTION TO PROGRAMMING",  46, "N"),
#     (2023,"Sem2", "MAT1830", "DISCRETE MATHEMATICS FOR COMPUTER SCIENCE",  42, "N"),
#     (2023,"Sem2", "FIT2101", "SOFTWARE ENGINEERING PROCESS AND MANAGEMENT", 78, "D"),
#     (2023,"Sem2", "FIT2107", "SOFTWARE QUALITY AND TESTING", 50, "P"),
#     (2024,"Summer", "FIT3171", "DATABASES",  68, "C"),
#     (2024,"Sem1", "FIT2085", "FUNDAMENTALS OF ALGORITHMS FOR ENGINEERS",  57, "P"),
#     (2024,"Sem1", "MAT1830", "DISCRETE MATHEMATICS FOR COMPUTER SCIENCE",  60, "C"),
#     (2024,"Sem2", "ENG1005", "ENGINEERING MATHEMATICS", 57, "P"),
#     (2024,"Sem2", "FIT2004", "ALGORITHMS AND DATA STRUCTURES", 42, "N"),
#     (2025,"Sem1", "FIT2004", "ALGORITHMS AND DATA STRUCTURES",  54, "P"),
#     (2025,"Sem1", "FIT2099", "OBJECT ORIENTED DESIGN AND IMPLEMENTATION",  82, "HD"),
#     (2025,"Sem1", "FIT3159", "COMPUTER ARCHITECTURE",  83,"HD"),
#     (2025,"Sem2", "FIT2100", "OPERATING SYSTEMS", 82, "HD"),
#     (2025,"Sem2", "FIT3003", "BUSINESS INTELLIGENCE AND DATA WAREHOUSING", 71, "D"),
#     (2025,"Sem2", "FIT3138", "REAL TIME ENTERPRISE SYSTEMS", 84, "HD"),
#     (2025,"Sem2", "FIT3176", "ADVANCED DATABASE DESIGN", 74, "D"),
#     (2026,"Summer", "FIT3175", "USABILITY",  None, "INCOMPLETE"),
#     (2026,"Sem1", "FIT3170", "SOFTWARE ENGINEERING PRACTICE", None, "INCOMPLETE"),
#     (2026,"Sem1", "FIT3077", "SOFTWARE ENGINEERING: ARCHITECTURE AND DESIGN",  None, "INCOMPLETE"),
#     (2026,"Sem1", "FIT4165", "COMPUTER NETWORKS",  None, "INCOMPLETE"),
#     (2026,"Sem1", "ENG0001", "ENGINEERING CONTINUOUS PROFESSIONAL DEVELOPMENT", None, "INCOMPLETE")
# ]

# def seed_units():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     # Add new columns if upgrading an existing db
#     for col in ["year INTEGER", "semester TEXT", "code TEXT", "score INTEGER"]:
#         try:
#             c.execute(f"ALTER TABLE units ADD COLUMN {col}")
#         except:
#             pass

#     inserted = 0
#     skipped = 0

#     for year, sem, code, title, score, grade in units:
#         existing = c.execute(
#             "SELECT id FROM units WHERE code = ? AND year = ? AND semester = ?",
#             (code, year, sem)
#         ).fetchone()

#         if existing:
#             print(f"  SKIP: {code} ({sem} {year})")
#             skipped += 1
#             continue

#         c.execute(
#             "INSERT INTO units (year, semester, code, name, score, grade) VALUES (?, ?, ?, ?, ?, ?)",
#             (year, sem, code, title, score, grade)
#         )
#         print(f"  OK: {code} ({sem} {year}) — {grade}")
#         inserted += 1

#     conn.commit()
#     conn.close()
#     print(f"\nDone. {inserted} inserted, {skipped} skipped.")

if __name__ == "__main__":
    seed_applications()