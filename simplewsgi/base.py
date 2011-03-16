from werkzeug.wrappers import Request, Response

class BaseView(object):
    def __init__(self, *args):
        super(BaseView, self).__init__()
    
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch(request)
        return response(environ, start_response)
    
    def dispatch(self, request):
        return Response('Base view')