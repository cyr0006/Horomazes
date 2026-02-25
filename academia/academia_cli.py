import click
from dotenv import cli
from agent import get_db_module

db_module = get_db_module("academia")

@cli.command()
@click.argument("name")
@click.option("--type", default="other", help="achievement/feedback/project/promotion/other")
@click.option("--impact", default=None)
def log_event(name, enrolment_period, grade=None, notes=None):
    """Log a unit."""
    db_module.log_event(name, enrolment_period, grade=grade, notes=notes)
    click.echo(f"Unit logged: {name}")