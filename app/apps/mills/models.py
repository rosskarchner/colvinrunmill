from google.appengine.ext import db, blobstore
from tipfy.appengine.db.properties import SlugProperty

from geo.geomodel import GeoModel

class Mill(GeoModel):
	name = db.StringProperty()
	slug=SlugProperty(name)
	year=db.StringProperty()
	mill_no=db.IntegerProperty()
	description=db.TextProperty()


