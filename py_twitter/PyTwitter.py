from .utils import ParamsUtils
from .utils.API import API


class PyTwitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.api = API(consumer_key, consumer_secret, token_key, token_secret)

    def post_tweet(self, new_tweet):
        """
        Method that perform a post of tweet.

        Params:
        ----------
        new_tweet : String

            - Text of tweet.

        Return:
        ----------
        response : Dict

            - Information of tweet published
        """
        params = {
            'status': new_tweet
        }

        response = self.api.post('statuses/update.json', params)
        return response

    def search(self, query, **kwargs):
        """
        Method that perform search for tweets.

        Params:
        ----------
        query : String

            - Text of tweet.
        lang : String

            - Language of tweets.
        tweet_mode : String

            - Tweet text mode.

        Return:
        ----------
        tweets : List

            - List of tweets found.
        """
        lang = kwargs.get('lang', 'pt-br')
        tweet_mode = kwargs.get('tweet_mode', 'extended')
        params = {
            'q': query,
            'lang': lang,
            'tweet_mode': tweet_mode,
        }

        response = self.api.get('search/tweets.json', params)
        tweets = response['statuses']
        return tweets

    def show(self, id_tweet, **kwargs):
        """
        Method that searches for a specific tweet.

        Params:
        ----------
        id_tweet : String

            - ID of tweet.
        tweet_mode : String

            - Tweet text mode.

        Return:
        ----------
        response : Dic

            - Tweet found.
        """
        tweet_mode = kwargs.get('tweet_mode', 'extended')
        params = {
            'id': id_tweet,
            'tweet_mode': tweet_mode,
        }

        response = self.api.get('statuses/show.json', params)
        return response

    def show_lookup(self, ids):
        """
        Method that searches for multiple tweets by id.

        Params:
        ----------
        ids : List

            - List of tweet ids.
        tweet_mode : String

            - Tweet text mode.

        Return:
        ----------
        tweets : List

            - List of tweets found.
        """
        tweets = []
        for id in ids:
            tweet = self.show(id)
            tweets.append(tweet)

        return tweets

    def retweet(self, id_tweet, **kwargs):
        """
        Method that searches for multiple tweets by id.

        Params:
        ----------
        id_tweet : List

            - ID of tweet.
        trim_user : String

            - Return data about users (False) or just the ID (True)

        Return:
        ----------
        response : Dict

            - Tweet retwweted.
        """
        trim_user = kwargs.get('trim_user', True)
        params = {
            'trim_user': ParamsUtils.format_params_booleans(trim_user)
        }

        url = 'statuses/retweet/{}.json'.format(str(id_tweet))
        response = self.api.post(url, params)
        return response

    def filter_tweets(self, **kwargs):
        """
        Method that filters tweets.

        Params:
        ----------
        track : String

            - Filtering options

        Return:
        ----------
        tweets : Dict

            - Filtered tweets.
        """
        track = kwargs.get('track', '')
        params = {
            'track': track,
        }

        response = self.api.post_stream('statuses/filter.json', params)
        tweets = response['result']['places']
        return tweets

    def get_followers(self, **kwargs):
        """
        Method that fetches a user's followers.

        Params:
        ----------
        user_id : String

            - ID of user.
        screen_name: String

            - The screen name of the user for whom to return results.
        cursor : String

            - For results to be divided into pages.
        count : String

            - Number of users returned per page.
        skip_status : String

            - Whether to remove user status or not.
        include_user_entities : String

            - The user object entities node will not be included when set to false.

        Return:
        ----------
        response : List

            - List of users(followers).
        """
        user_id = kwargs.get('user_id', '')
        screen_name = kwargs.get('screen_name', '')
        cursor = kwargs.get('cursor', -1)
        count = kwargs.get('count', 20)
        skip_status = kwargs.get('skip_status', '')
        include_user_entities = kwargs.get('include_user_entities', '')

        params = {
            'user_id': user_id,
            'screen_name': screen_name,
            'cursor': cursor,
            'count': count,
            'skip_status': ParamsUtils.format_params_booleans(skip_status),
            'include_user_entities': ParamsUtils.format_params_booleans(include_user_entities),
        }

        response = self.api.get('followers/list.json', params)
        return response

    def geo(self, query):
        """
        Method that perform search for tweets by geolocation.

        Params:
        ----------
        query : String

            - To search for places by name.

        Return:
        ----------
        tweets : List

            - List of tweets found.
        """
        params = {
            'query': query,
        }

        response = self.api.get('geo/search.json', params)
        tweets = response['result']['places']
        return tweets
