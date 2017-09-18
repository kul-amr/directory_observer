import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
import config as config


def create_conn():

    try:
        conn = sqlite3.connect(config.DB_PATH)
        return conn
    except StandardError as err:
        print err

    return None

def get_session():

    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

