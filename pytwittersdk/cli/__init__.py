import click
from .commands.start import start
from .commands.show import show
from .commands.search import search
from .commands.write_file import write_files


@click.group()
def cli():
    pass


cli.add_command(start)
cli.add_command(show)
cli.add_command(search)
cli.add_command(write_files)
