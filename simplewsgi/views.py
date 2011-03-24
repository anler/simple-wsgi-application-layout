from base import BaseView
from http import HttpResponse
from jinja2 import Environment, PackageLoader

jinja_env = Environment(loader=PackageLoader('simplewsgi', 'templates'),
                        extensions=['jinja2.ext.i18n'])

class IndexView(BaseView):
    def dispatch(self, request):
        context = {}
        response = jinja_env.get_template('index.html').render(context)
        return HttpResponse(response)
