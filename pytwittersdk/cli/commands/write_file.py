import click
from ..commands import py_twitter


@click.command('write_file', help='Method that writes a list of twitter ids or tweets dict into json or csv file.')
@click.option('--name', required=True, type=str, prompt='Name of file',
              help='Name of file')
@click.option('--file_format', required=True, type=str, prompt='Format of file(csv or json)',
              help='Format of file(csv or json)')
@click.option('--query', required=True, type=str, prompt='Text of tweet',
              help='Text of tweet')
def write_files(name, file_format, query):
    tweets = py_twitter.search(query)
    py_twitter.write_tweets(tweets, name, file_format)
    click.echo("Success")
