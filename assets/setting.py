"""
Initial configuration file for Twitter follower database
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "follower.db")
# ENGINE = create_engine(
#     "sqlite:///" + DATABASE_FILE,
#     encoding="utf-8",
#     echo=True,
# )
ENGINE = create_engine("sqlite:///:memory:")
Base = declarative_base()
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE,
    )
)
Base.query = session.query_property()


def init_db():
    import assets.models

    Base.metadata.create_all(bind=ENGINE)
