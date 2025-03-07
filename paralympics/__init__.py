import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import csv
from pathlib import Path

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):
    # create the Flask app
    app = Flask(__name__, instance_relative_config=True)

    # configure the Flask app (see later notes on how to generate your secret key)
    app.config.from_mapping(
        SECRET_KEY='nvMKOvpawAtHtCyhMeBylg',
        # Set the location of the database file called paralympics.sqlit
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instance_path))

    if test_config is None:
    # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
    # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app. instance_path)
    except OSError:
        pass

    # Initialise Flask with the SQLAlchemy database extension
    db.init_app(app) 

    # We must import the models defined in the models module
    from paralympics.models import User, Region, Event
    from data.create_db_add_data import create_db
    # Create tables in the database
    # create_all does not update tables if they are already in the database
    with app.app_context():
        #create_db()
        #add_data_from_csv()

        # Register the routes with the app in the context
        from paralympics import routes
    return app

