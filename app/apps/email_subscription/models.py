from datetime import datetime
from base64 import urlsafe_b64encode
from os import urandom

from app import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(8), unique=True)
    email = db.Column(db.String(255), unique=True)
    confirmed = db.Column(db.Boolean(), default=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def confirm(self):
        self.confirmed = True

    def __init__(self, email, confirmed):
        hash = urlsafe_b64encode(urandom(10))[:8]
        self.hash = hash
        self.email = email
        self.confirmed = confirmed

    def __repr__(self):
        return '<Email %r>' % self.email
