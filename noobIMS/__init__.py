from datetime import timedelta

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# configure the flask app
app = Flask(__name__)

"""Generate a secret key with
$ python -c 'import secrets; print(secrets.token_hex())' """
app.secret_key = "6a2ca96237a23fd8b853c5c917241f071ffae536c7ac9bd"

app.permanent_session_lifetime = timedelta(minutes=5)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLAlchemy_TRACK_MODIFICATIONS"] = False

# Initialise the extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


"""These comments are to prevent my formatter or
someone else's moving this import to the top"""
from noobIMS import routes  # noqa: E402
from noobIMS.models.users import User  # noqa: E402

# create database
with app.app_context():
    db.create_all()
