from typing import Union, List
from .utils.API import API
from .utils import ParamsUtils
import json
import csv


class PyTwitter:
    """Class main of lib"""

    def __init__(self, consumer_key: str, consumer_secret: str,
                 token_key: str, token_secret: str):
        self.api = API(consumer_key, consumer_secret, token_key, token_secret)

    def post_tweet(self, new_tweet: str, in_reply_to_status_id: str,
                   attachment_url: str, media_ids: List[str], lat: str,
                   long: str, card_uri: str, place_id: str,
                   display_coordinates: bool, trim_user: bool = False,
                   enable_dmcommands: bool = False,
                   fail_dmcommands: bool = True,
                   possibly_sensitive: bool = False,
                   auto_populate_reply_metadata: bool = False):
        """
        Method that perform a post of tweet.

        Params:
        ----------
        `new_tweet (str):` Text of tweet.

        `in_reply_to_status_id (str):` The ID of an existing status 
            that the update is in reply to. `NOTE`: This parameter will be
            ignored unless the author of the Tweet this parameter references is
            mentioned within the status text.

        `attachment_url (str):` In order for a URL to not be counted
            in the status body of an extended Tweet.

        `media_ids (list[str]):` A comma-delimited list of media ids to associate
            with the Tweet.

        `lat (float):` The latitude to search around. It will be ignored if it is an
            invalid value (outside the range -90 and +90) and if it does not
            have the long parameter.

        `long (float):` The longitude to search around. It will be ignored if it is an
            invalid value (outside the range -180 and +180) and if it does not
            have the lat parameter.

        `card_uri (str):` Associate an ads card with the Tweet using the card uri
            value from any ads card response.

        `place_id (str):` A place in the world..

        `display_coordinates (bool):` Whether or not to put a pin on the exact
            coordinates a Tweet has been sent from.

        `trim_user (bool):` When set to either true , t or 1 , the response will
            include a user object including only the author's ID.

        `enable_dmcommands (bool):` When set to true, enables shortcode commands
            for sending Direct Messages as part of the status text to send
            a Direct Message to a user.

        `fail_dmcommands (bool):` When set to true, causes any status text that starts
            with shortcode commands to return an API error.

        `possibly_sensitive (bool):` If you upload Tweet media that might be
            considered sensitive content such as nudity, or medical procedures,
            you must set this value to true.

        `auto_populate_reply_metadata (bool):` If set to true and used with
            `in_reply_to_status_id`, leading `@mentions` will be looked up from
            the original Tweet, and added to the new Tweet from there. 

        Return:
        ----------
        response (dict): Information of tweet published
        """
        params = {
            'status': new_tweet,
            'in_reply_to_status_id': in_reply_to_status_id,
            'attachment_url': attachment_url,
            'media_ids': media_ids,
            'lat': lat,
            'long': long,
            'card_uri': card_uri,
            'place_id': place_id,
            'display_coordinates': display_coordinates,
            'trim_user': trim_user,
            'enable_dmcommands': enable_dmcommands,
            'fail_dmcommands': fail_dmcommands,
            'possibly_sensitive': possibly_sensitive,
            'auto_populate_reply_metadata': auto_populate_reply_metadata,
        }

        response = self.api.post('statuses/update.json', params)
        return response

    def search(self, query: str, lang: str = 'pt-br',
               tweet_mode: str = 'extended'):
        """Method that perform search for tweets.

        Params:
        ----------
        `query (str):` Text of tweet.

        `lang (str):` Language of tweets.

        `tweet_mode(str):` Tweet text mode.

        Return:
        ----------
        tweets (list): List of tweets.
        """
        params = {
            'q': query,
            'lang': lang,
            'tweet_mode': tweet_mode,
        }

        response = self.api.get('search/tweets.json', params)
        tweets = response['statuses']
        return tweets

    def show(self, id_tweet: str, tweet_mode: str = 'extended'):
        """Method that searches for a specific tweet.

        Params:
        ----------
        `id_tweet (str):` ID of tweet.

        `tweet_mode (str):` Tweet text mode.

        Return:
        ----------
        response (dict): Tweet.
        """
        params = {
            'id': id_tweet,
            'tweet_mode': tweet_mode,
        }

        response = self.api.get('statuses/show.json', params)
        return response

    def show_lookup(self, ids: List[str], tweet_mode: str = 'extended'):
        """Method that searches for multiple tweets by id.

        Params:
        ----------
        `ids (list):` List of tweet ids.

        `tweet_mode (str):` Tweet text mode.

        Return:
        ----------
        tweets (list): List of tweets.
        """
        tweets = []
        for id in ids:
            tweet = self.show(id, tweet_mode)
            tweets.append(tweet)

        return tweets

    def retweet(self, id_tweet: str, trim_user: str = None):
        """Method that searches for multiple tweets by id.

        Params:
        ----------
        `id_tweet (list):` Tweet id.

        `trim_user (str):` Return data about users (False) or just the ID (True)

        Return:
        ----------
        response (dict): Tweet retwweted.
        """
        trim_user = ParamsUtils.format_params_booleans(trim_user)
        params = {
            'trim_user': trim_user
        }
        url = 'statuses/retweet/{}.json'.format(str(id_tweet))
        response = self.api.post(url, params)
        return response

    def filter_tweets(self, track: str):
        """Method that filters tweets.

        Params:
        ----------
        `track (str):` Filtering options

        Return:
        ----------
        tweets (dict): Filtered tweets.
        """
        params = {
            'track': track,
        }

        response = self.api.post_stream('statuses/filter.json', params)
        tweets = response['result']['places']
        return tweets

    def get_followers(self, user_id: str, screen_name: str = "",
                      cursor: int = -1, count: int = 20,
                      skip_status: bool = True, include_user_entities: bool = True):
        """
        Method that fetches a user's followers.

        Params:
        ----------
        `user_id (str):` User id.

        `screen_name (str):` The screen name of the user for whom to return results.

        `cursor (int):` For results to be divided into pages.

        `count (int):` Number of users returned per page.

        `skip_status (bool):` Whether to remove user status or not.

        `include_user_entities (bool):` The user object entities node will not be included when set to false.

        Return:
        ----------
        response (list): List of users(followers).
        """
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

    def geo(self, lat: float, long: float,
            query: str, ip: float, max_results: int, granularity: str = "neighborhood"):
        """
        Method that Search for places that can be attached to a Tweet.

        Params:
        ----------
        `lat (float):` The latitude to search around. It will be ignored if it is an
            invalid value (outside the range -90 and +90) and if it does not
            have the long parameter.

        `long (float):` The longitude to search around. It will be ignored if 
            it is an invalid value (outside the range -180 and +180) and if
            it does not have the lat parameter.

        `query (str):` To search for places by name.

        `ip (float):` An IP address. Used when attempting to fix geolocation based 
            off of the user's IP address.

        `max_results (int):` Number max of results

        `granularity (str):` This is the minimal granularity of place types to 
            return and must be one of: neighborhood , city , admin or country.

        Return:
        ----------
        tweets (list): List of tweets found.
        """
        params = {
            'lat': lat,
            'long': long,
            'query': query,
            'ip': ip,
            'max_results': max_results,
            'granularity': granularity,
        }

        response = self.api.get('geo/search.json', params)
        tweets = response['result']['places']
        return tweets

    def write_tweets(self, tweets: list, file_name: str, file_format: str):
        """
        Method that writes a list of twitter ids or tweets dict into json or csv file.

        Params:
        ----------
        `tweets (List[str]) or (List[dict]):` TweetsId or TweetsDictionary.

        `file_name (str):` the name of the outputed file.

        `file_format (str):` should be csv or json
        
        """
        if type(tweets[0]) == str:
            tweets = self.show_lookup(tweets)
        if file_format == 'json':
            file = open(file_name + '.json', 'w')
            json.dump(tweets, file, indent=4)
            file.close()
        elif file_format == 'csv':
            keys = ['created_at', 'id_str', 'full_text', ['entities', 'hashtags'],
                        'lang', ['user', 'id_str', 'screen_name', 'location'],
                        'retweet_count', 'favorite_count', 'coordinates']
            converted_tweets = []
            for tweet in tweets:
                converted_tweets.append(self.__selected_keys(keys, tweet))

            with open(file_name + '.csv', 'w') as f:
                writer = csv.DictWriter(f, fieldnames=converted_tweets[0])
                writer.writeheader()
                writer.writerows(converted_tweets)

    def __selected_keys(self, keys:Union[str, list], tweet, key_complement: str = ''):
        """
        Method that writes a list of twitter ids or tweets dict into json or csv file.

        Params:
        ----------
        `keys (str) or (list):` tweet dict key  or tweet list of dict keys.

        `tweet (dict):` tweet dict to be filtered.

        `key_complement (str):` key to be added before the key name: complement_key.
        
        Return:
        ----------
        `tweet_dict (dict)`: tweet dict filtered with only the selected keys. 
        """
        tweet_dict = {}
        for key in keys:      
            if type(key) == str:
                tweet_dict[key_complement + key] = tweet[key] 
            elif type(key) == list:
                for sub_key in range(1, len(key)):
                    if type(key[sub_key]) == list:
                        tweet_dict.update(self.__selected_keys([key[sub_key]], tweet[key[0]], key_complement + key[0] + '_'))
                    else:
                        tweet_dict['{0}{1}_{2}'.format(key_complement, key[0], key[sub_key])] = tweet[key[0]][key[sub_key]]
        return tweet_dict
