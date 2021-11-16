import json
import time
import tweepy

SEARCH_NUM = 10


class Bot:
    def __init__(self):
        with open(r"./key_token.json", "r") as jf:
            load = json.load(jf)
            self.API_KEY = load["API_KEY"]
            self.API_SECRET_KEY = load["API_SECRET_KEY"]
            self.BEARER_TOKEN = load["BEARER_TOKEN"]
            self.ACCESS_TOKEN = load["ACCESS_TOKEN"]
            self.ACCESS_TOKEN_SECRET = load["ACCESS_TOKEN_SECRET"]


class TwitterBot(Bot):
    """Bot to tweet automatically"""

    def __init__(self, *args):
        super().__init__(*args)
        self.auth = tweepy.OAuthHandler(
            self.API_KEY,
            self.API_SECRET_KEY,
        )
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def post(self, text):
        """Post a message on Twitter

        Args:
            text: Content to tweet
        """
        tw = tweepy.API(self.auth)
        tw.update_status(status=text)

    def search_keyword(self):
        """Enter an account, topic, or keyword to search"""
        query = "(漫画好き OR 本好き)"
        tweet_items = tweepy.Cursor(
            self.api.search,
            q=query,
            tweet_mode="extended",
            result_type="mixed",
        ).items(SEARCH_NUM)

        return tweet_items

    def follow(self):
        """follow user account"""

        tweet_items = self.search_keyword()

        for tweet in tweet_items:
            try:
                self.api.create_friendship(tweet.user.screen_name)
                print(tweet.user.screen_name)
                # print(tweet.full_text)
                time.sleep(3)
            except Exception as e:
                print(e)

    def follow_back(self):
        """Return follow if followed"""
        for follower in tweepy.Cursor(self.api.followers).items():
            try:
                follower.follow()
            except Exception as e:
                print(e)
            time.sleep(3)
