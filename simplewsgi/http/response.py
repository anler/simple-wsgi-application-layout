from werkzeug.wrappers import BaseResponse
from werkzeug.wrappers import ETagResponseMixin
from werkzeug.wrappers import CommonResponseDescriptorsMixin
from werkzeug.wrappers import WWWAuthenticateMixin
from werkzeug.wrappers import ResponseStreamMixin

class HttpResponse(BaseResponse, ETagResponseMixin, ResponseStreamMixin,
            CommonResponseDescriptorsMixin, WWWAuthenticateMixin):
    
    default_mimetype = 'text/html'
    