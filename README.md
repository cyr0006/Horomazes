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

Commands:

- `init`: Initialise the database.
- `query <message>`: Ask the agent anything.
- `log-event <description> [--type <type>] [--impact <impact>]`
- `log-skill <name> [--level <level>] [--notes <notes>]`
- `log-goal <goal> [--by <target_date>]`
- `log-job <company> <role>`
- `chat`: Start an interactive conversation with the agent.
- Exit the chat with 'exit'

# Contact

Name: Aryan Cyrus
Ph: 0470311472
Email: Aryan.m10@yahoo.com
Website: [text](https://acyrus.netlify.app/)
