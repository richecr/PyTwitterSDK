import urllib.parse
import json
import requests
from requests_oauthlib import OAuth1
from .constants import api
from .utils import ParamsUtils


class PyTwitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.base_uri = api.URI_BASE
        self.base_uri_stream = api.URI_BASE_STREAM
        self.auth = self.conexao(
            consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        return OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    def novoTweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        params = {
            'status': query_codificada
        }

        uri = "{}/statuses/update.json".format(self.base_uri)
        response = requests.post(uri, auth=self.auth, params=params)
        response = response.json()
        return response

    def search(self, query, **kwargs):
        lang = kwargs.get('lang', 'pt-br')
        tweet_mode = kwargs.get('tweet_mode', 'extended')
        params = {
            'q': query,
            'lang': lang,
            'tweet_mode': tweet_mode,
        }

        uri = "{}/search/tweets.json".format(self.base_uri)
        response = requests.get(uri, auth=self.auth, params=params)
        response = response.json()
        tweetes = response['statuses']
        return tweetes

    def show(self, id_tweet, **kwargs):
        tweet_mode = kwargs.get('tweet_mode', 'extended')
        params = {
            'id': id_tweet,
            'tweet_mode': tweet_mode,
        }

        uri = "{}/statuses/show.json".format(self.base_uri)
        response = requests.get(uri, auth=self.auth, params=params)
        tweet = response.json()
        return tweet

    def show_lookup(self, ids):
        tweets = []
        for id in ids:
            tweet = self.show(id)
            tweets.append(tweet)

        return tweets

    def retweet(self, id_tweet, **kwargs):
        trim_user = kwargs.get('trim_user', True)

        params = {
            'trim_user': ParamsUtils.format_params_booleans(trim_user)
        }

        uri = "{}/statuses/retweet/{}.json".format(
            self.base_uri, str(id_tweet))
        response = requests.post(uri, auth=self.auth, params=params)
        tweet = response.json()
        return tweet

    def filter_tweets(self, **kwargs):
        track = kwargs.get('kwargs', '')

        params = {
            'track': track,
        }

        uri = "{}/statuses/filter.json".format(self.base_uri_stream)
        response = requests.post(
            uri, auth=self.auth, stream=True, params=params)
        response = response.json()
        tweets = response['result']['places']
        return tweets

    def get_followers(self, **kwargs):
        user_id = kwargs.get('user_id', '')
        cursor = kwargs.get('cursor', -1)
        count = kwargs.get('count', 20)
        skip_status = kwargs.get('skip_status', '')
        include_user_entities = kwargs.get('include_user_entities', '')

        params = {
            'user_id': user_id,
            'cursor': cursor,
            'count': count,
            'skip_status': ParamsUtils.format_params_booleans(skip_status),
            'include_user_entities': ParamsUtils.format_params_booleans(include_user_entities),
        }

        uri = "{}/followers/list.json".format(self.base_uri)
        response = requests.get(uri, auth=self.auth, params=params)
        users = response.json()
        return users

    def geo(self, query):
        params = {
            'query': query,
        }

        uri = "{}/geo/search.json".format(self.base_uri)
        response = requests.get(uri, auth=self.auth, params=params)
        response = response.json()
        tweets = response['result']['places']
        return tweets
