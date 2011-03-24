from os import path

PROJECT_ROOT = path.dirname(__file__)


TEMPLATE_PATH = path.join(PROJECT_ROOT, 'templates')


MIDDLEWARE_CLASSES = [
    ('werkzeug.wsgi.SharedDataMiddleware', 
                {'/img': path.join(PROJECT_ROOT, 'shared', 'images')}),
    ('middlewares.sample.SampleMiddleware',),
]