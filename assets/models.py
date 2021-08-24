from datetime import datetime

from sqlalchemy import Column, Date, Integer, String

from assets.setting import Base


class Follower(Base):
    """Tabel Information"""

    # TableNameの設定
    __tablename__ = "followers"
    # Column情報を設定
    id = Column(Integer, primary_key=True, autoincrement=False)
    screen_name = Column(String)
    user_id = Column(Integer)
    timestamp = Column(Date, default=datetime.now())
