from flask import Flask , request, render_template
import config as config
from backend.models import *
from backend.connect_db import *
from sqlalchemy import and_

def create_app(config):

    harness_app = Flask(__name__)
    harness_app.config.from_object(config)
    db.init_app(harness_app)
    db.create_all(app = harness_app)
    return harness_app

harness_app = create_app(config=config)

@harness_app.route('/')
def home():
    return "starting app!"

@harness_app.route('/logs',methods=['GET'])
def get_parsed_logs():

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if ((start_date is not None) and (end_date is not None)):
        session = get_session()
        logs_data_count = ParsedFile.query.count()
        logs_data = session.query(ParsedFile).\
            filter(and_(ParsedFile.created_date>=start_date,ParsedFile.created_date<end_date))\
            .order_by(ParsedFile.created_date.desc()).all()
    else:
        raise StandardError("Start or End date is not provided")

    return render_template('logs.html',logs_data=logs_data,total_logs=logs_data_count)

@harness_app.route('/users',methods=['GET'])
def get_all_users():

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if ((start_date is not None) and (end_date is not None)):
        print "dates as :", start_date, end_date
        session = get_session()
        users_data_count = User.query.count()
        users_data = session.query(User).filter(and_(User.created_date >= start_date, User.created_date < end_date))\
            .order_by(User.created_date.desc()).limit(100)
    else:
        raise StandardError("Start or End date is not provided")

    return render_template('users.html',users_data=users_data,total_users = users_data_count)
