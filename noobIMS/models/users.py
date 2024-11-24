from sqlalchemy import func

from noobIMS import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())

    def __init__(
        self, firstname: str, lastname: str, email: str, username: str, password: str
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"ID: {self.id}, Firstname: {self.firstname}, \
Lastname: {self.lastname}, Email address: {self.email}, \
Created on: {self.date_created}"
