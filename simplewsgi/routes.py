from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
from views import IndexView

url_map = Map([
    Rule('/', endpoint=IndexView)
])