from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import validators


class SubscriptionForm(Form):
    email = TextField(u'Email Address', validators=[validators.Email(),
                validators.length(max=255)])
