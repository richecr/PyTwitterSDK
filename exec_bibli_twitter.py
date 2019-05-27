from MyApiTwitter import Twitter

consumer_Key = '5seEmVC04JjQXSIQBIxPLrNsk'
consumer_Secret = 'Zl9ZA4RDidTFbgiZZVCLolV1vzmLuWONIKPn14KLWMSTEWStDZ'

token_Key = '855074511498170368-phycV4NNzwpOex7ZHg9d4Eo17N642Xd'
token_Secret = 'rY093cMYhYccUJ8QH6zCu60nZp6tbT7EzNVgbdoPsobXu'

twitter = Twitter(consumer_Key, consumer_Secret, token_Key, token_Secret)

#publicar = twitter.tweet('Olá Mundo')

pesquisa = twitter.search('São Paulo', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])