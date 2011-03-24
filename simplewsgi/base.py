from http import HttpRequest, HttpResponse

class BaseView(object):
    
    def __call__(self, environ, start_response, *params):
        request = HttpRequest(environ)
        response = self.dispatch(request, *params)
        return response(environ, start_response)
    
    def dispatch(self, request):
        return HttpResponse('Base view')