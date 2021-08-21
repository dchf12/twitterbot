import tweepy
import json


class Bot:
    def __init__(self):
        with open("./key_token.json", "r") as jf:
            load = json.load(jf)
            self.API_KEY = load["API_KEY"]
            self.API_SECRET_KEY = load["API_SECRET_KEY"]
            self.BEARER_TOKEN = load["BEARER_TOKEN"]
            self.ACCESS_TOKEN = load["ACCESS_TOKEN"]
            self.ACCESS_TOKEN_SECRET = load["ACCESS_TOKEN_SECRET"]


class TwitterBot(Bot):
    """
    Bot to tweet automatically
    """

    def __init__(self, *args):
        super().__init__(*args)
        # APIインスタンスを作成
        self.auth = tweepy.OAuthHandler(
            self.API_KEY,
            self.API_SECRET_KEY,
        )
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def post(self, text):
        """
        Post a message on Twitter
        """
        tw = tweepy.API(self.auth)
        # twitterへメッセージを投稿する
        tw.update_status(status=text)
