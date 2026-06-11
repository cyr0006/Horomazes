import click
from career import db_career as db_module

@click.group()
def career_cli():
    """Career agent commands."""
    pass

# Log a job application
@career_cli.command()
@click.argument("company")
@click.argument("role")
@click.option("--date-applied", default=None, help="Date applied (YYYY-MM-DD)")
@click.option("--status", default="applied", help="Application status")
@click.option("--notes", default=None, help="Additional notes")
def log_job(company, role, date_applied=None, status="applied", notes=None):
    """Log a job application."""
    db_module.log_job(company, role, date_applied=date_applied, notes=notes)
    click.echo(f"Application logged: {role} at {company}")