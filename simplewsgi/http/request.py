from werkzeug.wrappers import BaseRequest
from werkzeug.wrappers import AcceptMixin
from werkzeug.wrappers import ETagRequestMixin
from werkzeug.wrappers import UserAgentMixin
from werkzeug.wrappers import CommonRequestDescriptorsMixin
from werkzeug.wrappers import AuthorizationMixin

class HttpRequest(BaseRequest, AcceptMixin, ETagRequestMixin, 
            UserAgentMixin, CommonRequestDescriptorsMixin,
            AuthorizationMixin):
    pass