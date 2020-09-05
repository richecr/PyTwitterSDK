from py_twitter import PyTwitter
import json

with open('keys.json', 'r') as json_file:
    keys = json.load(json_file)

consumer_Key = keys['consumer_Key']
consumer_Secret = keys['consumer_Secret']

token_Key = keys['token_Key']
token_Secret = keys['token_Secret']

twitter = PyTwitter(consumer_Key, consumer_Secret, token_Key, token_Secret)

# Todos os tweets com a hastag.
tweets = twitter.search(query="real madrid")

print(tweets[0])

# Pegando apenas o texto(completo) do tweet.
tweets = map(lambda tweet: tweet['full_text'], tweets)

print(list(tweets))
