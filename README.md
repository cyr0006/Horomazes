# Horomazes — Personal AI Agent

A command-line AI agent that acts as a personal advisor across career, academia,
finance, and fitness. It combines structured database records with personal context
to give specific, data-driven advice rather than generic responses.

## How it works

The agent uses a coordinator pattern — a single entry point that sees all your data
across every domain and reasons across them. Career, academia, and finances are deeply
interconnected, and the coordinator reflects that.

Each message to the agent is backed by:

- **personal_context.md** — your background, goals, and narrative context
- **Domain context files** — structural info about each domain (grading scales, career positioning etc.)
- **SQLite databases** — structured records for jobs, units, and finances
- **Conversation history** — the current session is remembered turn by turn

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root:

   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

3. Initialise the databases:

   ```bash
   python agent.py init --agent career
   python agent.py init --agent academia
   python agent.py init --agent finance
   ```

4. Seed historical data (optional):
   ```bash
   python seed.py
   ```

## Talking to the agent

```bash
# One-off question
python agent.py query "Where do my career and academic situation intersect right now?"

# Interactive conversation (type 'exit' to quit)
python agent.py chat
```

## Logging data

### Career

```bash
python agent.py career log-job "Company" "Role Title" --notes "location: Melbourne VIC"
```

### Academia

```bash
# Add a new unit
python agent.py academia log-unit FIT3077 "SOFTWARE ENGINEERING: ARCHITECTURE AND DESIGN" --year 2026 --sem Sem1 --grade HD --score 85

# Update an existing unit
python agent.py academia update-unit FIT3077 "SOFTWARE ENGINEERING: ARCHITECTURE AND DESIGN" --year 2026 --sem Sem1 --grade HD --score 85
```

### Finance

```bash
python agent.py finance log-monthly-cost "2026-04" 2450.52 --notes "vehicle service and roadworthy"
```

## Keeping context up to date

The agent is only as good as the data it has. General rule: if it has a number
or a date, it should be a database record. If it's narrative or structural, it
lives in a markdown file.

| What                       | Where                          | How often          |
| -------------------------- | ------------------------------ | ------------------ |
| Goals, backstory, finances | `personal_context.md`          | When things change |
| Degree structure           | `academia/context-academia.md` | Rarely             |
| Career positioning         | `career/context-career.md`     | When things change |
| Finance snapshot           | `finance/context-finance.md`   | Monthly            |
| Job applications           | Career DB via CLI              | As you apply       |
| Unit grades                | Academia DB via CLI            | End of semester    |
| Monthly spend              | Finance DB via CLI             | Monthly            |

## Project structure

```
agent.py                        ← CLI entry point
coordinator/
    coordinator.py              ← context assembly and routing
    system-coordinator.md       ← coordinator system prompt
career/
    career_cli.py               ← career CLI commands
    db_career.py                ← career database
    context-career.md           ← career narrative context
    system-career.md            ← career system prompt
academia/
    academia_cli.py             ← academia CLI commands
    db_academia.py              ← academia database
    context-academia.md         ← academia narrative context
    system-academia.md          ← academia system prompt
finance/
    finance_cli.py              ← finance CLI commands
    db_finance.py               ← finance database
    context-finance.md          ← finance narrative context
    system-finance.md           ← finance system prompt
fitness/
    context-fitness.md          ← fitness narrative context
    system-fitness.md           ← fitness system prompt
personal_context.md             ← merged personal context (source of truth)
seed.py                         ← bulk data seeding scripts
requirements.txt
```

## Roadmap - coming soon

- [ ] Persistent conversation history across sessions
- [ ] Fitness DB and CLI (workouts, metrics)
- [ ] Transaction-level finance logging
- [ ] Job status update command (`career update-job`)
- [ ] Web UI

# Contact

Name: Aryan Cyrus
Ph: 0470311472
Email: Aryan.m10@yahoo.com
Website: [acyrus.netlify.appt](https://acyrus.netlify.app/)
