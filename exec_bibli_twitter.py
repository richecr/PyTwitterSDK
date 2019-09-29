from MyApiTwitter import Twitter

consumer_Key = '####'
consumer_Secret = '####'

token_Key = '####'
token_Secret = '####'

twitter = Twitter(consumer_Key, consumer_Secret, token_Key, token_Secret)

#publicar = twitter.tweet('Olá Mundo')

pesquisa = twitter.search('São Paulo', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
