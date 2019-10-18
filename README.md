# Biblioteca para usar a API do Twitter.
> Objetivo de facilitar o uso da api do twitter.

## Funções

* [Publicar no Tweet](https://github.com/Rickecr/BibliotecaTwitter#publicar-um-novo-twitter).
* [Buscar por tweets](https://github.com/Rickecr/BibliotecaTwitter#buscar-tweets).
* [Buscar um tweets específico]().
* [Buscar tweets de uma determinada localização]().
* [Filtrar tweets]().
* [Retweetar um tweet]().

## Como usar
> A biblioteca não se encontra no PyPI, então para usar em um de seus projetos, vai necessitar desses passos a seguir.

### Importar a biblioteca:

* Faça o clone do projeto: `git clone https://github.com/Rickecr/BibliotecaTwitter`.
* Mova o arquivo `MyApiTwitter.py` para onde está seu projeto.
* Você precisar instalar a biblioteca `oauth2` com o comando `pip install oauth2`. 
* Importe o arquivo para onde você vai usar: `from MyApiTwitter import Twitter`.
* Pronto, agora é só usar.

### Credenciais:

* Preencher consumer_Key, consumer_Secret, token_key e token_secret do twitter.
~~~~ 
from MyApiTwitter import Twitter
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

~~~~

### Publicar um novo Twitter:

~~~~
from MyApiTwitter import Twitter
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

mensagem = twitter.novoTweet("Olá Twitter")
   
~~~~

### Buscar Tweets:

~~~~
from MyApiTwitter import Twitter
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

# Primeiro parametro => Texto a ser procurado nos tweets.
# Segundo parametro => Idioma dos tweets.
busca = twitter.search("Champions League", "pt")

~~~~

### imprimir resultado da busca de tweest:

~~~~
from MyApiTwitter import Twitter
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

# Primeiro parametro => Texto a ser procurado nos tweets.
# Segundo parametro => Idioma dos tweets.
busca = twitter.search("Champions League", "pt")

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
~~~~

## Contribuir com o projeto:
Para contribuir é bem simples, basta seguir os passos de [CONTRIBUTING.md](https://github.com/Rickecr/BibliotecaTwitter/blob/master/CONTRIBUTING.md)
