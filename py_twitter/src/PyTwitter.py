import urllib.parse
import json
import requests
from requests_oauthlib import OAuth1
from .constants import api

class PyTwitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.base_uri = api.URI_BASE
        self.base_uri_stream = api.URI_BASE_STREAM
        self.auth = self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        return OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    def novoTweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        uri = self.base_uri + '/statuses/update.json?status=' + query_codificada
        response = requests.post(uri, auth=self.auth)
        response = response.json()
        return response

    def search(self, query, lang="pt-br", tweet_mode=""):
        query_codificada = urllib.parse.quote(query, safe='')
        uri = self.base_uri + '/search/tweets.json?q=' + query_codificada + '&tweet_mode=' + tweet_mode + '&lang=' + lang
        response = requests.get(uri, auth=self.auth)
        response = response.json()
        tweetes = response['statuses']
        return tweetes

    def show(self, query):
        uri = self.base_uri + '/statuses/show.json?id=%s&tweet_mode=extended' % query
        response = requests.get(uri, auth=self.auth)
        tweet = response.json()
        return tweet

    def show_lookup(self, ids):
        tweets = []
        for id in ids:
            tweet = self.show(id)
            tweets.append(tweet)

        return tweets

    def retweetar(self, query):
        uri = self.base_uri + "/statuses/retweet/" + str(query) + ".json"
        response = requests.post(uri, auth=self.auth)
        tweet = response.json()
        return tweet
    
    def filter(self, query):
        query_codificada = urllib.parse.quote(query, safe='')
        uri = self.base_uri_stream + '/statuses/filter.json?track=' + query_codificada
        response = requests.post(uri, auth=self.auth, stream=True)
        response = response.json()
        tweets = response['result']['places']
        return tweets
    
    def get_followers(self):
        uri = self.base_uri + "/followers/list.json"
        response = requests.get(uri, auth=self.auth)
        tweets = response.json()
        return tweets

    def geo(self, query):
        query_codificada = urllib.parse.quote(query, safe='')
        uri = self.base_uri + '/geo/search.json?query=' + query_codificada
        response = requests.get(uri, auth=self.auth)
        response = response.json()
        tweets = response['result']['places']
        return tweets
