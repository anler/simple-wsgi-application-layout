from werkzeug.local import Local, LocalManager

local = Local()
local_manager = LocalManager([local])
application = local('application')


def url_for(endpoint, _external=False, locale=None, **values):
    return local.url_adapter.build(endpoint, values,
                force_external=_external, locale=locale)