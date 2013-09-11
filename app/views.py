from flask import render_template, send_from_directory

from app import app
from apps.email_subscription.views import handle_subscription
from apps.email_subscription.forms import SubscriptionForm


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.jinja')


@app.route('/wristbands/', methods=['GET', 'POST'])
def wristbands():
    return render_template('wristbands.jinja')


@app.route('/resources/', methods=['GET', 'POST'])
def resources():
    return render_template('resources.jinja')


@app.route('/resources/<res>/', methods=['GET'])
def resource(res):
    return send_from_directory(app.config['RESOURCES_FOLDER'], res, as_attachment=True)


@app.route('/get-involved/', methods=['GET', 'POST'])
def get_involved():
    return render_template('get_involved.jinja')


@app.route('/big-march-2013/', methods=['GET', 'POST'])
def big_march():
    form = SubscriptionForm(prefix='bm')
    response = handle_subscription(form)
    if response:
        return response
    return render_template('big_march.jinja', form=form)


@app.route('/get-help/', methods=['GET', 'POST'])
def get_help():
    return render_template('get_help.jinja')
