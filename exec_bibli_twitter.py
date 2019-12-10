from py_twitter import PyTwitter
import json, requests
from requests_oauthlib import OAuth1

consumer_Key = 'XXX'
consumer_Secret = 'XXX'

token_Key = 'XXX'
token_Secret = 'XXX'

twitter = PyTwitter(consumer_Key, consumer_Secret, token_Key, token_Secret)
