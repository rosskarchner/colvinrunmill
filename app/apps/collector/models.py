from google.appengine.ext import db, blobstore
from tipfy.appengine.db.properties import SlugProperty
from google.appengine.api.images import get_serving_url


class Photo(db.Model):
	image = blobstore.BlobReferenceProperty()
	name= db.StringProperty()
	email=db.StringProperty()
	phone=db.StringProperty()
	location=db.GeoPtProperty()
	status=db.StringProperty(default="submitted")
	mill=db.ReferenceProperty()

	def thumb(self):
		return get_serving_url(str(self.image.key()), size=200)
		
	def link(self):
	    return get_serving_url(str(self.image.key()), size=768)
