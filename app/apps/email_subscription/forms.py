from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import validators


class SubscriptionForm(Form):
    name = TextField(u'Name', validators=[validators.length(max=255),
            validators.Required()])
    email = TextField(u'Email Address', validators=[validators.Email(),
            validators.length(max=255),
            validators.Required()])
