from fabric.api import local
from fabric.colors import cyan


def run():
    "Start app in debug mode for development"
    local('venv/bin/python run.py')
