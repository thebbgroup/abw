from os import urandom

from flask import flash, g, render_template, redirect, request

from app import app, db, mail
from app.forms import SubscribeForm
from app.models import Subscribe
from flask_mail import Message


@app.before_request
def before_request():
    # Add the subscription form to all requests:
    g.subscribe = SubscribeForm()


@app.route('/')
def home():
    return render_template('home.jinja')


@app.route('/wristbands/')
def wristbands():
    return render_template('wristbands.jinja')


@app.route('/resources')
def resources():
    return render_template('resources.jinja')


@app.route('/get-involved/')
def get_involved():
    return render_template('get_involved.jinja')


@app.route('/big-march-2013/')
def big_march():
    return render_template('big_march.jinja')


@app.route('/get-help/')
def get_help():
    return render_template('get_help.jinja')


def build_confirm_email(email_address, hash, url):
    url = '%s%s' % (url, hash)
    message = Message(subject='Email Subscription Confirmation')
    message.recipients = [email_address]
    message.sender = 'hello@test.com'

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
    message.sender = 'hello@test.com'
    message.body = '''
    Congratulations: You are now signed up to our newsletter!
    '''
    return message


@app.route('/subscribe/', methods=['POST'])
def subscribe():
    form = SubscribeForm()
    if not form.validate_on_submit():
        flash('Invalid email address')
        return redirect(request.referrer)

    email = request.form['email']

    # Check email isn't already subscribed:
    if not Subscribe.query.filter_by(email=email).first() is None:
        flash('This address is already subscribed!')
        return redirect(request.referrer)

    # Create 8 character random hex hash:
    hash = urandom(10).encode('hex')[:8]
    user = Subscribe(hash=hash, email=email, is_subscribed=False)

    db.session.add(user)
    db.session.commit()

    message = build_confirm_email(email, hash, request.url)
    mail.send(message)
    return render_template('email_sent.jinja')


@app.route('/subscribe/<hash>/')
def confirm_subscription(hash):
    user = Subscribe.query.filter_by(hash=hash).first()
    user.is_subscribed = True
    db.session.commit()
    message = build_success_email(user.email)
    mail.send(message)
    return render_template('subscribe_successful.jinja')
