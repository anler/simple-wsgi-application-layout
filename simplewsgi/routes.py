from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
import views

url_map = Map([
    Rule('/', endpoint=views.index_view),
    Rule('/static/<file>', endpoint='static', build_only=True)
])