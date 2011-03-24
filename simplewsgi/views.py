#from jinja2 import Environment, PackageLoader
from jinja2 import Environment, FileSystemLoader

from http import HttpResponse
import settings

#jinja_env = Environment(loader=PackageLoader('simplewsgi', 'templates'),
#                        extensions=['jinja2.ext.i18n'])
jinja_env = Environment(loader=FileSystemLoader(settings.TEMPLATE_PATH),
                        extensions=['jinja2.ext.i18n'])

def index_view(request):
    context = {}
    response = jinja_env.get_template('index.html').render(context)
    return HttpResponse(response)
