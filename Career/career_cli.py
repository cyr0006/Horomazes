# Log an event
import click
from dotenv import cli
from agent import get_db_module

db_module = get_db_module("career")

@cli.command()
@click.argument("description")
@click.option("--type", default="other", help="achievement/feedback/project/promotion/other")
@click.option("--impact", default=None)
def log_event(description, type, impact):
    """Log a career event."""
    db_module.log_event(description, type, impact)
    click.echo(f"Event logged: {description}")

# Log a skill
@cli.command()
@click.argument("name")
@click.option("--level", default="intermediate", help="beginner/intermediate/advanced/expert")
@click.option("--notes", default=None)
def log_skill(name, level, notes):
    """Log or update a skill."""
    db_module.log_skill(name, level, notes=notes)
    click.echo(f"Skill logged: {name} ({level})")

# Log a goal
@cli.command()
@click.argument("goal")
@click.option("--by", default=None, help="Target date e.g. 2025-12-31")
def log_goal(goal, by):
    """Log a career goal."""
    db_module.log_goal(goal, target_date=by)
    click.echo(f"Goal logged: {goal}")

# Log a job application
@cli.command()
@click.argument("company")
@click.argument("role")
def log_job(company, role):
    """Log a job application."""
    db_module.log_job(company, role)
    click.echo(f"Application logged: {role} at {company}")