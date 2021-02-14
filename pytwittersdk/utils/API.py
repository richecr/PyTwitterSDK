from requests_oauthlib import OAuth1
from ..constants import api
import requests


class API:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.base_uri = api.URI_BASE
        self.base_uri_stream = api.URI_BASE_STREAM
        self.auth = self.connection(
            consumer_key, consumer_secret, token_key, token_secret)

    def connection(self, consumer_key, consumer_secret, token_key, token_secret):
        return OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    def get(self, url, params):
        uri = "{}/{}".format(self.base_uri, url)
        response = requests.get(uri, auth=self.auth, params=params)
        response = response.json()
        return response

    def post(self, url, params):
        uri = "{}/{}".format(self.base_uri, url)
        response = requests.post(uri, auth=self.auth, params=params)
        response = response.json()
        return response

    def post_stream(self, url, params):
        uri = "{}/{}".format(self.base_uri_stream, url)
        response = requests.post(
            uri, auth=self.auth, stream=True, params=params)
        response = response.json()
        return response
