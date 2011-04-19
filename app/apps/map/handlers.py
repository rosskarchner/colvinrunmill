from werkzeug import cached_property

from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin




class IndexHandler(RequestHandler, Jinja2Mixin):
    def get(self):
    	
        return self.render_response('map/index.html')
