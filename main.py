import twitter_bot


def main():
    # init_db()

    tw_bot = twitter_bot.TwitterBot()
    tw_bot.follow()
    tw_bot.follow_back()


if __name__ == "__main__":
    main()
