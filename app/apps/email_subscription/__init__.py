from flask import Blueprint


email_subscription_app = Blueprint('email_subscription',
        __name__, template_folder='templates')

from . import views
