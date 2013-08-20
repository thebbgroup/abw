from flask_wtf import Form
from wtforms import TextField
from wtforms import validators


class SubscribeForm(Form):
    email = TextField(u'Email Address', validators=[validators.Email(),
                validators.length(max=80)])
