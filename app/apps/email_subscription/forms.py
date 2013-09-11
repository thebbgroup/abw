from flask import request
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import validators


class SubscriptionForm(Form):
    name = TextField(u'Name', validators=[validators.length(max=255),
            validators.Required()])
    email = TextField(u'Email Address', validators=[validators.Email(),
            validators.length(max=255),
            validators.Required()])

    def __init__(self, *args, **kwargs):
        if 'prefix' in kwargs:
            self.prefix = kwargs['prefix']
        super(SubscriptionForm, self).__init__(*args, **kwargs)

    def is_submitted(self):
        """Override to check that this particular form was submitted and not
        another on the same page"""
        return request and request.method in ('PUT', 'POST') and \
                ('%s-name' % self.prefix) in request.form and \
                ('%s-email' % self.prefix) in request.form
