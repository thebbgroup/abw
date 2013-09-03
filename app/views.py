from flask import g, render_template, redirect, url_for

from app import app
from app.apps.email_subscription import subscription_requested
from app.apps.email_subscription.forms import SubscriptionForm


@app.before_request
def before_request():
    # Add the subscription form to all requests:
    g.subscribe = SubscriptionForm()
    if subscription_requested(g.subscribe):
        return redirect(url_for('subscribe'))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.jinja')


@app.route('/wristbands/', methods=['GET', 'POST'])
def wristbands():
    return render_template('wristbands.jinja')


@app.route('/resources', methods=['GET', 'POST'])
def resources():
    return render_template('resources.jinja')


@app.route('/get-involved/', methods=['GET', 'POST'])
def get_involved():
    return render_template('get_involved.jinja')


@app.route('/big-march-2013/', methods=['GET', 'POST'])
def big_march():
    return render_template('big_march.jinja')


@app.route('/get-help/', methods=['GET', 'POST'])
def get_help():
    return render_template('get_help.jinja')


@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe():
    return render_template('email_sent.jinja')
