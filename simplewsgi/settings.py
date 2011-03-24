import os

PROJECT_ROOT = os.path.dirname(__file__)

MIDDLEWARE_CLASSES = [
    ('werkzeug.wsgi.SharedDataMiddleware', 
                {'/image': os.path.join(PROJECT_ROOT, 'shared', 'images')}),
    ('middlewares.sample.SampleMiddleware',),
]