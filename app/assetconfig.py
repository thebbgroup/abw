from os.path import dirname, join, realpath

from flask.ext.assets import Environment, Bundle

from app import app


environment = Environment(app)
environment.versions = 'hash'
manifest_path = realpath(join(dirname(__file__), '.static-manifest'))
environment.manifest = 'file://%s' % manifest_path
environment.cache = False

css_main = Bundle(
    'css/main.css',
    filters='cssmin',
    output='css/main.%(version)s.css'
)

js_head = Bundle(
    'js/modernizr.custom.min.js',
    output='js/head.%(version)s.js'
)

js_foot = Bundle(
    'https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js',
    Bundle(
        'js/scripts.js',
        filters='jsmin'
    ),
    output='js/main.%(version)s.js'
)
