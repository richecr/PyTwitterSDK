import click
import json


@click.command('start', help='Method that will save the keys')
@click.option('--consumer_key', '-ck', required=True, type=str, prompt='Consumer Key',
              help='Consumer Key')
@click.option('--consumer_secret', '-cs', required=True, type=str, prompt='Consumer Secret',
              help='Consumer Secret')
@click.option('--token_key', '-tk', required=True, type=str, prompt='Token Key',
              help='Token Key')
@click.option('--token_secret', '-ts', required=True, type=str, prompt='Token Secret',
              help='Token Secret')
def start(consumer_key, consumer_secret, token_key, token_secret):
    keys = {}
    keys['consumer_Key'] = consumer_key
    keys['consumer_Secret'] = consumer_secret
    keys['token_Key'] = token_key
    keys['token_Secret'] = token_secret

    with open('keys_cli.json', 'w') as json_file:
        json.dump(keys, json_file)
    click.echo("Saved keys!")
