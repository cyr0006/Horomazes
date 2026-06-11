
import sqlite3

units = [
    (2026,"Sem2", "FIT3170", "SOFTWARE ENGINEERING PRACTICE PART 2", None, "UPCOMING", ""),
    (2026,"Sem2", "FIT4701", "SOFTWARE ENGINEERING RESEARCH PROJECT PART 1",  None, "UPCOMING", ""),
    (2026,"Sem2", "FIT4005", "IT REASEARCH AND INNOVATION METHODS",  None, "UPCOMING", "MANADATORY LEVEL 4 ELECTIVE"),
    (2026,"Sem2", "FITxxxx", "SOME ELECTIVE OF MY CHOOSING",  None, "UPCOMING", "CAN TAKE AT ANY TIME"),
    (2027,"Sem1", "FIT4701", "SOFTWARE ENGINEERING RESEARCH PROJECT PART 2",  None, "UPCOMING", ""),
    (2027,"Sem1", "FIT4002", "SOFTWARE ENGINEERING STUDIO PROJECT part 1",  None, "UPCOMING", ""),
    (2027,"Sem2", "FIT4002", "SOFTWARE ENGINEERING STUDIO PROJECT part 2",  None, "UPCOMING", ""),
]

def seed_units():
    conn = sqlite3.connect('academia.db')
    c = conn.cursor()

    # Add new columns if upgrading an existing db
    for col in ["year INTEGER", "semester TEXT", "code TEXT", "score INTEGER", "notes TEXT"]:
        try:
            c.execute(f"ALTER TABLE units ADD COLUMN {col}")
        except:
            pass

    inserted = 0
    skipped = 0

    for year, sem, code, title, score, grade, notes in units:
        existing = c.execute(
            "SELECT id FROM units WHERE code = ? AND year = ? AND semester = ?",
            (code, year, sem)
        ).fetchone()

        if existing:
            print(f"  SKIP: {code} ({sem} {year})")
            skipped += 1
            continue

        c.execute(
            "INSERT INTO units (year, semester, code, name, score, grade, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (year, sem, code, title, score, grade, notes)
        )
        print(f"  OK: {code} ({sem} {year}) — {grade}")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nDone. {inserted} inserted, {skipped} skipped.")
    




if __name__ == "__main__":
    seed_units()
