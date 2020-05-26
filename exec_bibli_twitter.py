from py_twitter import PyTwitter
import json, requests

with open('keys.json', 'r') as json_file:
    keys = json.load(json_file)

consumer_Key = keys['consumer_Key']
consumer_Secret = keys['consumer_Secret']

token_Key = keys['token_Key']
token_Secret = keys['token_Secret']

twitter = PyTwitter(consumer_Key, consumer_Secret, token_Key, token_Secret)
