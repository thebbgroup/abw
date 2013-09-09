import logging
import os

from flask import Flask, render_template
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

from webassets.loaders import PythonLoader


logging.basicConfig()

app = Flask(__name__)
app.config.from_pyfile('settings/common.py')


if os.getenv('FLASK_CONFIG'):
    app.config.from_envvar('FLASK_CONFIG')

if app.debug:
    logging.getLogger().setLevel(logging.DEBUG)

db = SQLAlchemy(app)

mail = Mail(app)

# static assets
assets = PythonLoader('app.assetconfig').load_environment()
bundles = PythonLoader('app.assetconfig').load_bundles()

for bundle_name, bundle in bundles.items():
    assets.register(bundle_name, bundle)


@app.context_processor
def debug_context():
    "Notifies templates that they're in debug mode"
    return dict(debug=app.debug)


@app.context_processor
def ga_context():
    "Notifies templates that they're in debug mode"
    return dict(google_analytics_id=app.config['GOOGLE_ANALYTICS_ID'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.jinja'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.jinja'), 500

import views

from apps.email_subscription import email_subscription_app
app.register_blueprint(email_subscription_app, url_prefix='/subscribe')
