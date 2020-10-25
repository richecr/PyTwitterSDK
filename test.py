from py_twitter import PyTwitter
twitter = PyTwitter("3qif9AJj8xf2QeQwyErT0dPM2", "pHubz8UbAyAG0ufM4bJq16hXGvQgHX9EnMR1nGx7Z0vc7v8FqX",
                    "2220145722-JunnTXLDiFC4vIiyVXQ2uN5TJoivvsWvfuixnbl", "gktLPpxctFqKMYm0b9MZ3bVzAMGEuDHZhpUGEQKtZ5Bk3")


# Search for tweets
response = twitter.filter_tweets(track="twitter")
#tweets = twitter.geo(query="são paulo", max_results=200, granularity = "city")
#tweets = twitter.geo(query="são paulo", max_results=200, granularity = "admin")
#tweets = twitter.geo(query="são paulo", max_results=200, granularity = "country")
#tweets = twitter.geo(lat="são paulo", long="")
#tweets = twitter.geo(ip="são paulo")

# Print repose to see if retweet was with success
print(response)
