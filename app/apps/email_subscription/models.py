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
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    confirmed = db.Column(db.Boolean(), default=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    bigmarch = db.Column(db.Boolean(), default=False)
    __table_args__ = (db.UniqueConstraint('email', 'bigmarch'),)

    def confirm(self):
        self.confirmed = True
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(self, form):
        sub = Subscription(name=form.name.data,
                email=form.email.data,
                bigmarch=(form.prefix == 'bm'))
        db.session.add(sub)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise DuplicateSubscription()
        return sub

    def __repr__(self):
        return '<Subscription %r %r>' % (self.name, self.email)
