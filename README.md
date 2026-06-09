# Aryan's AI Agent

# Description

An AI agent which is able to advise the user based on their current situtation.

An AI agent is as good as the context it is given, hence this agent uses 4 sources of information for its context window:

- prompts/system.md: This tells the LLM who it is and what its job is.
- prompts/context.md: This tells the AI through prose what the background and story of the user is
- data/career.db: This keeps a record of the users goals, events, job applications and skills in a structured database
- The agent also remembers the content of the current converation so each message has the preceding messages as background information

NOTE: at this stage each converation is divorced, when you exit the chat nothing is changed in the context window unless specifically done by user.

# Installation

1. Install requirements.txt
2. create a .env file and place ANTHROPIC_API_KEY=[your API key]
3. Open the terminal and write python agent.py init

With these 3 steps the setup is complete.

# Usage

# Usage

## Talking to the agent

- `python agent.py query "<message>"` — one-off question through the coordinator
- `python agent.py chat` — interactive conversation with the coordinator (type `exit` to quit)

## Database setup

- `python agent.py init --agent career` — initialise the career DB
- `python agent.py init --agent academia` — initialise the academia DB
- `python agent.py init --agent finance` — initialise the finance DB

## Career commands

- `python agent.py career log-event "<description>" [--type <type>] [--impact <impact>]`
- `python agent.py career log-skill "<name>" [--level <level>] [--notes <notes>]`
- `python agent.py career log-goal "<goal>" [--by <target_date>]`
- `python agent.py career log-job "<company>" "<role>"`

## Academia commands

- `python agent.py academia log-unit <code> "<name>" --year <year> --sem <sem> [--grade <grade>] [--score <score>] [--notes <notes>]`
- `python agent.py academia update-unit <code> "<name>" --year <year> --sem <sem> [--grade <grade>] [--score <score>] [--notes <notes>]`

## Updating context

The agent's intelligence is only as good as the data it has. Keep these up to date:

- **personal_context.md** — your backstory, values, long-term goals. Edit manually when something significant changes.
- **academia/context-academia.md** — degree structure and grading scale. Rarely needs editing.
- **Career DB** — log jobs, skills, events, and goals via CLI as they happen.
- **Academia DB** — update unit grades at the end of each semester via `update-unit`.
- **finance/context-finance.md** — update your financial snapshot manually each month until a finance DB is in place.

# Contact

Name: Aryan Cyrus
Ph: 0470311472
Email: Aryan.m10@yahoo.com
Website: [acyrus.netlify.appt](https://acyrus.netlify.app/)
