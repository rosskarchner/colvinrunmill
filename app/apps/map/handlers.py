from werkzeug import cached_property

from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin
from apps.mills.models import Mill
from apps.collector.models import Photo

from google.appengine.ext import db



class IndexHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        mills=Mill.proximity_fetch(Mill.all(),
		    db.GeoPt(38.968780,-77.293140),
		    max_results=20
		    )
        photos=photos=Photo.all().filter('status =', 'approved').order('-added')
        return self.render_response('map/index.html', mills=mills, photos=photos)
