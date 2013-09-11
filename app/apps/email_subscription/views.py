from flask import abort, g, redirect, render_template, request, url_for
from flask.ext.mail import Message

from app import app, db, mail
from . import email_subscription_app as sub_app
from .models import Subscription, DuplicateSubscription
from .forms import SubscriptionForm


@app.before_request
def before_request():
    # Add the subscription form to all requests:
    g.subscribe = SubscriptionForm(prefix='news')
    handle_subscription(g.subscribe)


def handle_subscription(form):
    if form.validate_on_submit():
        try:
            sub = Subscription.create(form)
        except DuplicateSubscription:
            form.email.errors.append('This address is already subscribed!')
        else:
            mail.send(confirmation_msg(sub))
            return redirect(url_for('email_subscription.subscribe'))


@sub_app.route('/requested/', methods=['GET', 'POST'])
def subscribe():
    return render_template('subscribe/requested.jinja')


@sub_app.route('/confirmed/', methods=['GET', 'POST'])
def confirmed():
    return render_template('subscribe/confirmed.jinja')


@sub_app.route('/<hash>/', methods=['GET', 'POST'])
def confirm(hash):
    sub = Subscription.query.filter_by(hash=hash).first()
    if not sub:
        abort(404)

    if request.method == 'POST':
        sub.confirm()
        mail.send(success_msg(sub))
        return redirect(url_for('email_subscription.confirmed'))

    return render_template('subscribe/confirm.jinja')


def confirmation_msg(sub):
    # _external is to add domain to result of url_for() lookup:
    url = url_for('email_subscription.confirm',
            hash=sub.hash,
            _external=True,
            _method='GET')

    msg = Message(subject='Email Subscription Confirmation')
    msg.recipients = [sub.email]
    msg.sender = 'hello@thebbgroup.org'

    msg.body = '''
    We received a request to subscribe this email address to our newsletter -
    please go to this unique URL to confirm:

    %s

    If you didn't sign up, please ignore this email and you won't receive
    anything else from us. ''' % url

    return msg


def success_msg(sub):
    msg = Message(subject='You are now signed up to the newsletter!')
    msg.recipients = [sub.email]
    msg.sender = 'hello@thebbgroup.org'
    msg.body = '''
    Congratulations: You are now signed up to our newsletter!
    '''
    return msg
