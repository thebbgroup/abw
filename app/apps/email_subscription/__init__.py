from flask import Blueprint, flash, render_template, request, url_for
from flask.ext.mail import Message

from app import db, mail
from .models import Subscription


email_subscription_app = Blueprint('email_subscription',
        __name__, template_folder='templates')


def build_confirm_email(email_address, url):
    message = Message(subject='Email Subscription Confirmation')
    message.recipients = [email_address]
    message.sender = 'hello@thebbgroup.org'

    message.body = '''
    We received a request to subscribe this email address to our newsletter -
    please go to this unique URL to confirm:

    %s

    If you didn't sign up, please ignore this email and you won't receive
    anything else from us. ''' % url

    return message


def build_success_email(email_address):
    message = Message(subject='You are now signed up to the newsletter!')
    message.recipients = [email_address]
    message.sender = 'hello@thebbgroup.org'
    message.body = '''
    Congratulations: You are now signed up to our newsletter!
    '''
    return message


@email_subscription_app.route('/subscribe/<hash>/', methods=['GET', 'POST'])
def confirm_subscription(hash):
    subscribe = Subscription.query.filter_by(hash=hash).first()
    subscribe.confirm()
    db.session.commit()
    message = build_success_email(subscribe.email)
    mail.send(message)
    return render_template('subscribe_successful.jinja')


def subscription_requested(form):
    if form.validate_on_submit():
        # Check email isn't already subscribed:
        email = request.form['email']
        if Subscription.query.filter_by(email=email).first():
            flash('This address is already subscribed!')
            return False
        subscribe = Subscription(email=email, confirmed=False)
        db.session.add(subscribe)
        db.session.commit()

        # _external is to add domain to result of url_for() lookup:
        message = build_confirm_email(email, url_for(
            'email_subscription.confirm_subscription',
            hash=subscribe.hash, _external=True))

        mail.send(message)
        return True
    else:
        if form['email'].data:
            flash('Invalid email address')
        return False
