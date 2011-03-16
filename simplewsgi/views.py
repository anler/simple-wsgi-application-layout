from base import BaseView, Response
from jinja2 import Environment, PackageLoader

jinja_env = Environment(loader=PackageLoader('simplewsgi', 'templates'))

class IndexView(BaseView):
    
    def dispatch(self, request):
        context = {}
        return Response(jinja_env.get_template('index.html').render(context),
                        mimetype='text/html')