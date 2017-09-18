import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'harness.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
