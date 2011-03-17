from werkzeug.exceptions import HTTPException
from werkzeug.wsgi import SharedDataMiddleware

from utils import local, local_manager
import settings
import routes

class Application(object):
    """Core wsgi application"""
    def __init__(self):
        super(Application, self).__init__()
        local.application = self
        
        # self.dispatch = SharedDataMiddleware(self.dispatch, {
        #     '/static': settings.STATIC_PATH
        # })
    
    def __call__(self, *args):
        return self.dispatch(*args)
    
    def dispatch(self, environ, start_response):
        local.application = self
        url_adapter = routes.url_map.bind_to_environ(environ)
        local.url_adapter = url_adapter
        try:
            endpoint, params = url_adapter.match()
            return endpoint().__call__(environ, start_response, *params)
        except HTTPException, e:
            return e(environ, start_response)
        finally:
            local_manager.cleanup()

