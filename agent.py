import click
import os
from dotenv import load_dotenv
import openai
import db
load_dotenv()
client = openai.OpenAI()

def load_system_prompt():
    with open("system_prompt.txt", "r") as f:
        return f.read()
def load_personal_context():
    try:
        with open("prompt/context.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
def ask(user_message):
    system = load_system_prompt()
    db_context = db.get_context_block()
    personal_context = load_personal_context()
    
    full_message = f"{personal_context}\n\n{db_context}\n\n---\n\n{user_message}"
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": full_message}]
    )
    return response.content[0].text
@click.group()
def cli():
    """Your personal career agent."""
    pass

@cli.command()
def init():
    """Initialise the database."""
    db.init_db()
    click.echo("Database initialised.")

@cli.command()
@click.argument("message")
def query(message):
    """Ask the agent anything."""
    click.echo("\nThinking...\n")
    response = ask(message)
    click.echo(response)

@cli.command()
@click.argument("description")
@click.option("--type", default="other", help="achievement/feedback/project/promotion/other")
@click.option("--impact", default=None)
def log_event(description, type, impact):
    """Log a career event."""
    db.log_event(description, type, impact)
    click.echo(f"Event logged: {description}")

@cli.command()
@click.argument("name")
@click.option("--level", default="intermediate", help="beginner/intermediate/advanced/expert")
@click.option("--notes", default=None)
def log_skill(name, level, notes):
    """Log or update a skill."""
    db.log_skill(name, level, notes=notes)
    click.echo(f"Skill logged: {name} ({level})")

@cli.command()
@click.argument("goal")
@click.option("--by", default=None, help="Target date e.g. 2025-12-31")
def log_goal(goal, by):
    """Log a career goal."""
    db.log_goal(goal, target_date=by)
    click.echo(f"Goal logged: {goal}")

@cli.command()
@click.argument("company")
@click.argument("role")
def log_job(company, role):
    """Log a job application."""
    db.log_job(company, role)
    click.echo(f"Application logged: {role} at {company}")

if __name__ == "__main__":
    cli()
