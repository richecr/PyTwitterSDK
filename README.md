# PyTwitter

> Objective to facilitate the use of the twitter API.

## [Twitter API](https://developer.twitter.com/en/docs):

> The twitter API has several features. You can take a look and suggest implementing some functionality in the library.

### Install:

The library is not yet to be downloaded via `pip` or another python package manager. But it can be used as follows:

#### Import the library:

- Clone the project: `git clone https://github.com/Rickecr/PyTwitter`.
- Move the `PyTwitter.py` file to where your project.
- Install library dependencies: `pip install -r requirements.txt`
- Import the file `from PyTwitter import PyTwitter`.
- Okay, now just use it.

### Credentials:

- Fill `consumer_Key`, `consumer_Secret`, `token_key` and `token_secret` of twitter.

```python
from PyTwitter import PyTwitter
twitter = PyTwitter(consumer_key, consumer_secret, token_key, token_secret)
```

### Functions:

- [Post a tweet](#post-to-tweet).
- [Search for tweets](#search-for-tweets).
- [Search for a specific tweet]().
- [Search for tweets from a specific location]().
- [Filter tweets]().
- [Retweet a tweet]().

### Post to tweet:

```python
from PyTwitter import PyTwitter
twitter = PyTwitter(consumer_key, consumer_secret, token_key, token_secret)

mensagem = twitter.post_tweet("Hello twitter")
```

### Search for tweets:

```python
from py_twitter import PyTwitter
twitter = PyTwitter(consumer_key, consumer_secret, token_key, token_secret)


# Search for tweets
tweets = twitter.search(query="real madrid", lang="pt-br", tweet_mode="extended")

# Print all tweets
print(tweets)

# Print the first Tweet
print(tweets[0])

```

## Contributing:

To contribute is very simple, just follow the steps of [CONTRIBUTING.md](https://github.com/Rickecr/BibliotecaTwitter/blob/master/CONTRIBUTING.md)
