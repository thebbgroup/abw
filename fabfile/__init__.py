from fabric.api import local
from fabric.colors import cyan


def run():
    "Start app in debug mode for development"
    local('FLASK_CONFIG=settings/dev.py venv/bin/python run.py')
