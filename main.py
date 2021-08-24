from datetime import datetime

import twitter_bot
from assets.setting import init_db, session
from assets.models import Follower


def main():
    # init_db()

    tw_bot = twitter_bot.TwitterBot()
    tw_bot.follow()
    tw_bot.follow_back()

    # 取得データをツイート
    # tw_bot.post("test")

    # データベースに保存


def add_data(tweet):

    db_follower = Follower(id=0, screen_name="", user_id=0, timestamp=datetime.now())
    session.add(db_follower)
    # database.session().add_all(users)

    session.commit()


if __name__ == "__main__":
    main()
