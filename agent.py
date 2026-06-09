"""
AI Agent
A command-line tool to help you manage and grow in your career, academia, fitness, and finance.

By Aryan Cyrus

Commands:
- `init --agent <agent>`: Initialise the database for an agent.
- `query <message>`: Ask the coordinator anything.
- `chat`: Start an interactive conversation with the coordinator.
- `career log-event <description> --type <type> --impact <impact>`
- `career log-skill <name> --level <level> --notes <notes>`
- `career log-goal <goal> --by <target_date>`
- `career log-job <company> <role>`
- `academia log-unit <code> <name> ...`
- Exit chat with 'exit'
"""

import click
from dotenv import load_dotenv
load_dotenv()

import coordinator
from career.career_cli import career_cli
from academia.academia_cli import academia_cli
# from fitness.fitness_cli import fitness_cli
# from finance.finance_cli import finance_cli


def get_db_module(agent):
    if agent == "career":
        from career import db_career
        return db_career
    elif agent == "academia":
        from academia import db_academia
        return db_academia
    elif agent == "finance":
        from finance import db_finance
        return db_finance
    elif agent == "fitness":
        from fitness import db_fitness
        return db_fitness
    else:
        raise ValueError(f"Unknown agent: {agent}")


# ── CLI ───────────────────────────────────────────────────────────────────────

@click.group()
def cli():
    """Aryan's personal AI agent."""
    pass


@cli.command()
@click.option("--agent", default="career", help="Which agent DB to initialise (career/academia/fitness/finance)")
def init(agent):
    """Initialise the database for an agent."""
    db_module = get_db_module(agent)
    db_module.init_db()
    click.echo(f"Database initialised for: {agent}")


@cli.command()
@click.argument("message")
def query(message):
    """Ask the coordinator a one-off question."""
    click.echo("\nThinking...\n")
    response = coordinator.ask(message)
    click.echo(response)


@cli.command()
def chat():
    """Start an interactive conversation with the coordinator."""
    history = []
    click.echo("\nCoordinator ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue

        reply, history = coordinator.chat_turn(history, user_input)
        click.echo(f"\nAgent: {reply}\n")


# ── Sub-command groups ────────────────────────────────────────────────────────

cli.add_command(career_cli, name="career")
cli.add_command(academia_cli, name="academia")
# cli.add_command(fitness_cli, name="fitness")
# cli.add_command(finance_cli, name="finance")


if __name__ == "__main__":
    cli()