import click
from dotenv import cli
from academia import db_academia

@click.group()
def academia_cli():
    """Academia agent commands."""
    pass
@academia_cli.command()
@click.argument("name")
@click.option("--enrolment_period", default=None, help="Enrolment period e.g. Sem1 2023")
@click.option("--grade", default=None)
@click.option("--notes", default=None)
def log_unit(name, enrolment_period, grade=None, notes=None):
    """Log a unit."""
    db_academia.log_unit(name, enrolment_period, grade=grade, notes=notes)
    click.echo(f"Unit logged: {name}")