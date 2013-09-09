from datetime import datetime
from base64 import urlsafe_b64encode
from os import urandom

from sqlalchemy.exc import IntegrityError

from app import db


def token():
    return urlsafe_b64encode(urandom(10))[:8]


class DuplicateSubscription(Exception):
    pass


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(8), unique=True, default=token)
    email = db.Column(db.String(255), unique=True)
    confirmed = db.Column(db.Boolean(), default=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def confirm(self):
        self.confirmed = True
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(self, email):
        sub = Subscription(email=email)
        db.session.add(sub)
        try:
            db.session.commit()
        except IntegrityError:
            raise DuplicateSubscription()
        return sub

    def __repr__(self):
        return '<Email %r>' % self.email
