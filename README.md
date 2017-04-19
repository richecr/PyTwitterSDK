# BibliotecaTwitter
Permiti publicar e fazer buscar no twitter.


---------------------------------------------------------

//Importa a biblioteca.

from biblioteca_twitter import Twitter

//Coloca o consumer_Key, consumer_Secret, token_key e token_secret do twitter: (https://apps.twitter.com/app/13500222/keys) Criei uma conta.
//Com as 4 chaves vc coloca nas variáveis. OBS=> Para a pessoa que usar seu aapp para ela publicar ele precisa está logada na conta dela.
//O usuário não precisa saber as 4 chaves.

consumer_Key = ''

consumer_Secret = ''

token_Key = ''

token_Secret = ''

//Instânciei a classe Twitter e defini seus parâmetros.

twitter = Twitter(consumer_Key, consumer_Secret, token_Key, token_Secret)

//Vai na classe Twitter e executa o método 'novoTweet', que recebe como parâmetro a mensagem.

publicar = twitter.novoTweet('Olá Universo')

//Acessa o método 'search' da classe Twitter, que recebe dois parâmetros(1-Texto da pesquisa
//2-O idioma).

pesquisa = twitter.search('São Paulo', 'pt')

//Aqui ele imprimi o resultado da pesquisa.

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
