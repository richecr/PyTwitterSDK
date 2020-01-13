# PyTwitter
> Objetivo de facilitar o uso da API do twitter.

### Instalação:

A biblioteca ainda não se encontra para ser baixada por meio do `pip` ou de outro gerenciador de pacotes python.
Mas pode ser utilizada da seguinte maneira:

#### Importar a biblioteca:

* Faça o clone do projeto: `git clone https://github.com/Rickecr/BibliotecaTwitter`.
* Mova o arquivo `PyTwitter.py` para onde está seu projeto.
* Você precisar instalar a biblioteca `oauth2` com o comando `pip install oauth2`. 
* Importe o arquivo para onde você vai usar: `from PyTwitter import PyTwitter`.
* Pronto, agora é só usar.

### Primeira coisa a fazer: Preencher suas credenciais

* Preencher `consumer_Key`, `consumer_Secret`, `token_key` e `token_secret` do twitter.

~~~~python
from PyTwitter import PyTwitter
twitter = PyTwitter(consumer_key, consumer_secret, token_key, token_secret)
~~~~

### Funções

* [Publicar no Tweet](#publicar-um-novo-twitter).
* [Buscar por tweets](#buscar-tweets).
* [Buscar um tweets específico]().
* [Buscar tweets de uma determinada localização]().
* [Filtrar tweets]().
* [Retweetar um tweet]().

### Publicar um novo Twitter:

~~~~python
from PyTwitter import PyTwitter
twitter = PyTwitter(consumer_key, consumer_secret, token_key, token_secret)

mensagem = twitter.novoTweet("Olá Twitter")
~~~~

### Buscar Tweets:

~~~~python
from PyTwitter import PyTwitter
twitter = PyTwitter(consumer_key, consumer_secret, token_key, token_secret)

# Primeiro parametro => Texto a ser procurado nos tweets.
# Segundo parametro => Idioma dos tweets.
busca = twitter.search("Champions League", "pt")
~~~~

## Contribuir com o projeto:
Para contribuir é bem simples, basta seguir os passos de [CONTRIBUTING.md](https://github.com/Rickecr/BibliotecaTwitter/blob/master/CONTRIBUTING.md)
