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

def ask(user_message):
    system = load_system_prompt()
    context = db.get_context_block()
    full_message = f"{context}\n\n---\n\n{user_message}"
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": full_message}
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

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
