from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialise the flask app
app = Flask(__name__)

"""Generate a secret key with
$ python -c 'import secrets; print(secrets.token_hex())' """
app.secret_key = "6a2ca96237a23fd8b853c5c917241f071ffae536c7ac9bd"

app.permanent_session_lifetime = timedelta(minutes=5)

"""This is done to prevent my formatter or
someone else's moving this import to the top"""
if True:
    from noobIMS import routes


# database stuff
db = SQLAlchemy()  # create it
"""Where the sql files will be"""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# app.config["SQLALCHEMY_BINDS"] = "database"
db.init_app(app)

# dont output to teminal on every change
app.config["SQLAlchemy_TRACK_MODIFICATIONS"] = False


# create database
with app.app_context():
    db.create_all()
