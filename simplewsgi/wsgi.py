from werkzeug.exceptions import HTTPException
from werkzeug.wsgi import SharedDataMiddleware

from http import HttpRequest
from utils import local, local_manager
import settings
import routes

class Application(object):
    
    def __init__(self):
        super(Application, self).__init__()
        local.application = self
        
        for middleware in settings.MIDDLEWARE_CLASSES:
            modules = middleware[0].split('.')
            cls = modules.pop()
            options = middleware[1:]
            try:
                module = __import__('.'.join(modules), {}, {}, [cls])
                cls = getattr(module, cls)
                self.dispatch = cls(self.dispatch, *options)
            except ImportError:
                raise
    
    def __call__(self, *args):
        return self.dispatch(*args)
    
    def dispatch(self, environ, start_response):
        local.application = self
        url_adapter = routes.url_map.bind_to_environ(environ)
        local.url_adapter = url_adapter
        try:
            endpoint, params = url_adapter.match()
            response = endpoint(HttpRequest(environ), *params)
            return response(environ, start_response)
        except HTTPException, e:
            return e(environ, start_response)
        finally:
            local_manager.cleanup()

