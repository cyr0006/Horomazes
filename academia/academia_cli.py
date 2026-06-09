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


@academia_cli.command()
@click.argument("code")
@click.argument("name")
@click.option("--year", type=int, help="Year of the unit")
@click.option("--sem", help="Semester of the unit")
@click.option("--grade", help="Grade for the unit")
@click.option("--score", type=int, help="Score for the unit")
@click.option("--notes", help="Additional notes for the unit")
def update_unit(code, name, year, sem, score=None, grade=None, notes=None):
    """Update an existing unit."""
    db_academia.update_unit(code, name, year, sem, score=score, grade=grade, notes=notes)
    click.echo(f"Unit updated: {code} - {name}")