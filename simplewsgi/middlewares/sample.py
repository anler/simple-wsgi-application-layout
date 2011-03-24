
class SampleMiddleware(object):
    
    def __init__(self, app):
        super(SampleMiddleware, self).__init__()
        self.__app = app
    
    def __call__(self, environ, start_response):
        print 'Sample middleware...'
        return self.__app(environ, start_response)
    