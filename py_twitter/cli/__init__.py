import click
from .commands.search import search

@click.group()
def cli():
	pass

cli.add_command(search)