import click
from ..commands import py_twitter


@click.command('search', help='Method that perform search for tweets')
@click.option('--query', required=True, type=str, prompt='Text of tweet',
              help='Text of tweet')
def search(query):
    tweets = py_twitter.search(query)
    click.echo(tweets)
