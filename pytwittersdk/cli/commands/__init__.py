import json
from ...PyTwitter import PyTwitter

with open('keys.json', 'r') as json_file:
    keys = json.load(json_file)

consumer_Key = keys['consumer_Key']
consumer_Secret = keys['consumer_Secret']

token_Key = keys['token_Key']
token_Secret = keys['token_Secret']

py_twitter = PyTwitter(consumer_Key, consumer_Secret, token_Key, token_Secret)
