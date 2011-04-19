
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from models import Mill
from apps.collector.models import Photo


class MarkersJS(RequestHandler, Jinja2Mixin):
    def get(self):
    	mills=Mill.all()
    	return self.render_response('mills/markers.js', mills=mills)
        
        
class MillPage(RequestHandler, Jinja2Mixin):
	def get(self, mill_no, slug):
		mill=Mill.get_by_key_name(mill_no)
		photos=Photo.all().filter('mill =', mill).filter('status =', 'approved')
		return self.render_response('mills/single.html', mill=mill, photos=photos)


