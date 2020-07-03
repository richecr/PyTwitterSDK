import urllib.parse
from requests_oauthlib import OAuth1
from .constants import api
from .utils import ParamsUtils
from .utils.API import API


class PyTwitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.api = API(consumer_key, consumer_secret, token_key, token_secret)

    def post_tweet(self, new_tweet):
        params = {
            'status': new_tweet
        }

        response = self.api.post('statuses/update.json', params)
        return response

    def search(self, query, **kwargs):
        lang = kwargs.get('lang', 'pt-br')
        tweet_mode = kwargs.get('tweet_mode', 'extended')
        params = {
            'q': query,
            'lang': lang,
            'tweet_mode': tweet_mode,
        }

        response = self.api.get('search/tweets.json', params)
        tweetes = response['statuses']
        return tweetes

    def show(self, id_tweet, **kwargs):
        tweet_mode = kwargs.get('tweet_mode', 'extended')
        params = {
            'id': id_tweet,
            'tweet_mode': tweet_mode,
        }

        response = self.api.get('statuses/show.json', params)
        return response

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

        url = 'statuses/retweet/{}.json'.format(str(id_tweet))
        response = self.api.post(url, params)
        return response

    def filter_tweets(self, **kwargs):
        track = kwargs.get('track', '')
        params = {
            'track': track,
        }

        response = self.api.post_stream('statuses/filter.json', params)
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

        response = self.api.get('followers/list.json', params)
        return response

    def geo(self, query):
        params = {
            'query': query,
        }

        response = self.api.get('geo/search.json', params)
        tweets = response['result']['places']
        return tweets
