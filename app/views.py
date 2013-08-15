from flask import render_template

from app import app


@app.route('/')
def home():
    return render_template('home.jinja')


@app.route('/wristbands/')
def wristbands():
    return render_template('wristbands.jinja')


@app.route('/')
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
