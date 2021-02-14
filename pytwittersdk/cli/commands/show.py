import click


@click.command('show', help='Method that searches for a specific tweet')
@click.option('--id_tweet', '-id', required=True, type=str, prompt='ID of tweet',
              help='ID of tweet')
@click.option('--tweet_mode', '-mode', required=True, type=str, prompt='Tweet text mode',
              help='Tweet text mode')
def show(id_tweet, tweet_mode):
    from ..commands.pytwitter import py_twitter
    tweet = py_twitter.show(id_tweet, tweet_mode)
    click.echo(tweet)
