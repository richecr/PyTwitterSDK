# PyTwitterSDK
A Python SDK for the [API Twitter](https://developer.twitter.com/en). 

The [Twitter API](https://developer.twitter.com/en/docs) has several features. You can take a look and suggest implementing some functionality in the library.
It can be either a feature of the twitter API or even a feature that you think is important, one that you've used a lot and want an easier way to use.

### Install:

The library is not yet to be downloaded via `pip`(yet) or another python package manager. But it can be used as follows:

#### Import the library:

- Clone the project: `git clone https://github.com/Rickecr/PyTwitter`.
- Install library dependencies: `pip install -r requirements.txt`
- Move the `PyTwitter.py` file to where your project.
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

### Search for a specific tweet
> TODO

### Search for tweets from a specific location
> TODO

### Filter tweets
> TODO

### Retweet a tweet
> TODO

## Contributing:

To contribute is very simple, just follow the steps of [CONTRIBUTING.md](https://github.com/Rickecr/BibliotecaTwitter/blob/master/CONTRIBUTING.md)
