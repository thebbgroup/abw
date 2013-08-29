import socket

DEBUG = True

SECRET_KEY = 'r\xe1\xf7S\x95`z\xa8C/\xb8m\xde\xfb\x1dbk\x0b\xed\x16\x0b\xd8\xee\xea'

SQLALCHEMY_DATABASE_URI = 'sqlite:///abw.db'

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = 'web'

AUTH_USERS = {'admin': 'foo'}

DEFAULT_MAIL_SENDER = 'hello@%s' % socket.getfqdn()

ASSETS_DEBUG = False

GOOGLE_ANALYTICS_ID = 'foo'
