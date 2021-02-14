import click


@click.command('search', help='Method that perform search for tweets')
@click.option('--query', '-q', required=True, type=str, prompt='Text of tweet',
              help='Text of tweet')
def search(query):
    from ..commands.pytwitter import py_twitter
    tweets = py_twitter.search(query)
    click.echo(tweets)
