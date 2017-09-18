from sqlalchemy import Column,ForeignKey,Integer,String,Float,DateTime,Boolean
from flask_sqlalchemy import SQLAlchemy
import datetime as dt

#new sqlalchemy object
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    email = Column(String(30),nullable=False)
    created_date = Column(DateTime,nullable=False,default=dt.datetime.now())

class ParsedFile(db.Model):
    __tablename__ = 'parsed_files'
    id = Column(Integer,primary_key=True,autoincrement=True)
    filename = Column(String(200),nullable=False)
    file_created_date = Column(DateTime,nullable=False)
    parse_success = Column(Boolean,nullable=False)
    parse_message = Column(String(2000),nullable=False)
    create_date = Column(DateTime,nullable=False,default=dt.datetime.now())
