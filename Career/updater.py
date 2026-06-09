import sqlite3

DB_PATH = "career/career.db"

jobs = [
    ("Northrop Grumman",        "Intern - Engineering Certification",                       "2026-05-26", "haven't heard back, likely intakes are later in year",  "location: Australia"),
    ("Northrop Grumman",        "Intern - Engineering",                                     "2026-05-26", "haven't heard back, likely intakes are later in year",  "location: Australia"),
    ("Macquarie Group",         "2026/2027 Macquarie Summer Internship Technology Program", "2026-05-26", "haven't heard back, likely intakes are later in year",  "location: Sydney NSW"),
    ("Stripe",                  "Software Engineer, Intern",                                "2026-05-26", "haven't heard back, likely intakes are later in year",  "location: Australia"),
    ("ANZ",                     "Pre Register - 2026/27 Summer Intern Program",             "2026-05-26", "haven't heard back, likely intakes are later in year",  "location: Australia"),
    ("TASTY HOTPOT CLAYTON",    "Data Analyst",                                             "2026-04-07", "Never responded",                                       "location: Clayton VIC"),
    ("KPMG",                    "2026/27 KPMG Vacationer Program - Technology & Digital",   "2026-04-07", "haven't heard back, likely intakes are later in year",  "location: Melbourne VIC"),
    ("Deloitte",                "Deloitte Cyber Vacationer Program | 2026/27",              "2026-03-06", "haven't heard back, likely intakes are later in year",  "location: Melbourne VIC"),
    ("Quantium",                "Quantium Data Analytics Virtual Experience Program",       "2026-02-10", "haven't heard back, likely intakes are later in year",  "location: Melbourne VIC"),
    ("Airwallex",               "2026/27 Software Engineering Intern Program",              "2026-03-06", "haven't heard back, likely intakes are later in year",  "location: Melbourne VIC"),
    ("SEEK Grad",               "2026/27 EY Vacationer Program - Computer Science",        "2026-03-06", "haven't heard back, likely intakes are later in year",  "location: Melbourne VIC"),
    ("BHP",                     "BHP 2026 Intern Program",                                  "2026-03-06", "haven't heard back, likely intakes are later in year",  "location: Melbourne VIC"),
    ("Breen Printing",          "Web-to-Print Workflow Developer",                          "2026-02-19", "Never responded",                                       "location: Healesville VIC"),
    ("Future Events Lab",       "Fully Remote - Part Time Analyst / Developer",             "2026-02-17", "Never responded",                                       "location: Carlton VIC — Remote"),
    ("Ottica AI",               "Technical Support & Hardware Technician",                  "2026-02-17", "Never responded",                                       "location: Brunswick East VIC"),
    ("Private Advertiser",      "IT Support Technician (Part-Time)",                        "2026-02-19", "Never responded",                                       "location: Chadstone VIC"),
    ("Valui Healthcare",        "Developer & AI Branding",                                  "2026-02-12", "Never responded",                                       "location: Dandenong South VIC"),
    ("Moose Toys",              "Moose Intern Program",                                     "2026-02-11", "Never responded",                                       "location: Melbourne VIC"),
    ("Eastern Health",          "Data Engineer - Research",                                 "2026-02-07", "Never responded",                                       "location: Box Hill VIC"),
    ("Tiny Technologies",       "Intern QA Engineer",                                       "2026-02-07", "Never responded",                                       "location: Brisbane QLD"),
    ("Peoplebank Australia",    "Data Analyst (PowerBI/Snowflake/Alteryx/Matillion)",       "2026-01-23", "Never responded",                                       "location: Dandenong VIC"),
    ("Vanguard Group Pty Ltd",  "Junior Application Engineer",                              "2026-01-22", "Never responded",                                       "location: Melbourne VIC"),
    ("NewChurchTek Pty Ltd",    "Casual Software Systems Support",                          "2026-01-22", "Never responded",                                       "location: Melbourne VIC"),
    ("PANDA",                   "Data Systems Administrator (Data & Solutions) - Remote",   "2025-12-17", "Rejected",                                              "location: Melbourne VIC"),
    ("Nova Systems Pty Ltd",    "Expressions of Interest - 2027 Graduate Opportunities",    "2025-12-14", "Rejected",                                              "location: Melbourne VIC"),
    ("Hordern Consulting",      "SQL Developer",                                            "2025-12-07", "Never responded",                                       "location: Melbourne VIC"),
    ("QEC",                     "Business Intelligence Analyst",                            "2025-11-25", "Never responded",                                       "location: Noble Park VIC"),
]

def seed_applications():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    inserted = 0
    for company, role, date, status, notes in jobs:
        existing = c.execute(
            "SELECT id FROM jobs WHERE company = ? AND role = ?",
            (company, role)
        ).fetchone()
        if existing:
            print(f"  SKIP: {company} — {role}")
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
    seed_applications()