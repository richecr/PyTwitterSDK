import urllib.parse
import json, requests
from requests_oauthlib import OAuth1

class PyTwitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.auth = OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    def novoTweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')  # Para pesquisar com sinais(ex: #, acentos etc).
        response = requests.post('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, auth=self.auth)
        response = response.json()
        return response

    def search(self, query, lang="pt-br", tweet_mode=""):
        query_codificada = urllib.parse.quote(query, safe='')  # Para pesquisar com sinais(ex: #, acentos etc).
        response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&tweet_mode=' + tweet_mode + '&lang=' + lang, auth=self.auth)
        response = response.json()
        tweetes = response['statuses']
        return tweetes

    def filter(self, query):
        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request('https://stream.twitter.com/1.1/statuses/filter.json?locations=' + query_codificada)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['result']['places']
        return tweets

    def geo(self, query):
        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/geo/search.json?query=' + query_codificada)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['result']['places']
        return tweets

    def show(self, query):
        uri = 'https://api.twitter.com/1.1/statuses/show.json?id=%s&tweet_mode=extended' % query
        requisicao = self.cliente.request(uri)
        decodificar = requisicao[1].decode()
        tweets = json.loads(decodificar)
        return tweets
    
    def show_lookup(self, ids):
        tweets = []
        for id in ids:
            uri = 'https://api.twitter.com/1.1/statuses/show.json?id=%s&tweet_mode=extended' % id
            requisicao = self.cliente.request(uri)
            decodificar = requisicao[1].decode()
            tweets = json.loads(decodificar)
            tweets.append(tweets)

        return tweets

    def retweetar(self, query):
        url = "https://api.twitter.com/1.1/statuses/retweet/"+str(query) + ".json"
        requisicao = self.cliente.request(url, method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto