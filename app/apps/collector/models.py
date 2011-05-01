from google.appengine.ext import db, blobstore
from tipfy.appengine.db.properties import SlugProperty
from google.appengine.api.images import get_serving_url
from geo.geomodel import GeoModel



class Photo(GeoModel):
	image = blobstore.BlobReferenceProperty()
	name= db.StringProperty()
	status=db.StringProperty(default="submitted")
	mill=db.ReferenceProperty()
	added=db.DateTimeProperty(auto_now_add=True)

	def thumb(self):
		return get_serving_url(str(self.image.key()), size=200)
		
	def link(self):
	    return get_serving_url(str(self.image.key()), size=768)
