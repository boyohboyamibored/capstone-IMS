from sqlalchemy import func

from noobIMS import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    fName = db.Column(db.String(50), nullable=False)
    lName = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    passwd = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())

    def __init__(self, fName: str, lName: str, email: str, username: str, passwd: str):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.username = username
        self.passwd = passwd

    def __str__(self):
        return f"ID: {self.id}, Firstname: {self.fName}, \
Lastname: {self.lName}, Email address: {self.email}, \
Created on: {self.date_created}"
