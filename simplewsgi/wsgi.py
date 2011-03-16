from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException
import routes

class Application(object):
    """Core wsgi application"""
    def __init__(self):
        super(Application, self).__init__()
    
    def __call__(self, *args):
        return self.dispatch(*args)
    
    def dispatch(self, environ, start_response):
        urls = routes.url_map.bind_to_environ(environ)
        try:
            endpoint, args = urls.match()
            return endpoint(*args).__call__(environ, start_response)
        except HTTPException, e:
            return e(environ, start_response)