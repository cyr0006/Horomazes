import click
from finance import db_finance as db_module

@click.group()
def finance_cli():
    """Finance agent commands."""
    pass

# Log a monthly cost
@finance_cli.command()
@click.argument("month")
@click.argument("amount", type=float)
@click.option("--notes", default=None, help="Additional notes")
def log_monthly_cost(month, amount, notes=None):
    """Log a monthly cost."""
    db_module.log_monthly_cost(month, amount, notes=notes)
    click.echo(f"Monthly cost logged: {amount} for {month}")