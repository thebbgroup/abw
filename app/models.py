from flask import Flask

from app import db

app = Flask(__name__)


class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(8), unique=True)
    email = db.Column(db.String(80), unique=True)
    is_subscribed = db.Column(db.Boolean(), default=False)

    def __init__(self, hash, email, is_subscribed):
        self.hash = hash
        self.email = email
        self.is_subscribed = is_subscribed

    def __repr__(self):
        return '<Email %r>' % self.email
