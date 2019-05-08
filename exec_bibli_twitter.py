from MyApiTwitter import Twitter

consumer_Key = 'rrUDLNZVqv8DaWX6fkmNrB5V9'
consumer_Secret = 'R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7'

token_Key = '2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK'
token_Secret = 'AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW'

twitter = Twitter(consumer_Key, consumer_Secret, token_Key, token_Secret)

#publicar = twitter.tweet('Olá Mundo')

pesquisa = twitter.search('São Paulo', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
