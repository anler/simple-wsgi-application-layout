from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
from views import *

url_map = Map([
    Rule('/', endpoint=IndexView),
    Rule('/static/<file>', endpoint='static', build_only=True)
])