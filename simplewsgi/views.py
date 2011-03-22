from base import BaseView
from http import HttpResponse
#from jinja2 import Environment, PackageLoader
from jinja2 import Environment, FileSystemLoader
from os import path

TEMPLATE_PATH = path.join(path.dirname(__file__), 'templates')
#jinja_env = Environment(loader=PackageLoader('simplewsgi', 'templates'),
#                        extensions=['jinja2.ext.i18n'])
jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_PATH),
                        extensions=['jinja2.ext.i18n'])

class IndexView(BaseView):
    def dispatch(self, request):
        context = {}
        response = jinja_env.get_template('index.html').render(context)
        return HttpResponse(response)
