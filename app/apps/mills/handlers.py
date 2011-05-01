from google.appengine.ext import blobstore

from tipfy.appengine.blobstore import BlobstoreUploadMixin


from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from models import Mill
from apps.collector.models import Photo

import geojson


class MarkersJS(RequestHandler, Jinja2Mixin):
    def get(self):
        points=[]
    	mills=Mill.all()
    	for mill in mills:
    	    p=geojson.Point([mill.location.lat,mill.location.lon], properties={'name':mill.name, 'link':self.url_for('mills/single', mill_no=mill.mill_no, slug=mill.slug)})
    	    points.append(p)
    	
    	return Response(geojson.dumps(geojson.FeatureCollection(features=points)))
    	
    	return self.render_response('mills/markers.js', mills=mills)
        
        
class MillPage(RequestHandler, Jinja2Mixin):
	def get(self, mill_no, slug):
		mill=Mill.get_by_key_name(mill_no)
		nearby=[]
		try:
		    nearby=Mill.proximity_fetch(Mill.all(),
		    mill.location,
		    max_results=6
		    )
		except:
		    pass
		photos=Photo.all().filter('mill =', mill).filter('status =', 'approved')
		return self.render_response('mills/single.html', mill=mill, nearby=nearby[1:],photos=photos)


class AddPhoto(RequestHandler, Jinja2Mixin, BlobstoreUploadMixin):
    def get(self, mill_no, slug):
        mill=Mill.get_by_key_name(mill_no)
        upload_url = blobstore.create_upload_url(self.url_for('mills/addphoto', mill_no=mill.mill_no, slug=mill.slug))
        return self.render_response('mills/add_photo.html', mill=mill, upload_url=upload_url)
    
    def post(self, mill_no, slug):
    	blob=self.get_uploads('photo')[0]
    	mill=Mill.get_by_key_name(mill_no)
    	photo=Photo(image=blob,mill=mill,location=mill.location,
    	name=self.request.form['myname'])
    	photo.update_location()
    	photo.put()
    	
        response= self.redirect(self.url_for('photo-upload-thanks'), 302)
        response.data = ''
        return response
        
class PhotoUploadThanks(RequestHandler, Jinja2Mixin):
    def get(self):
    	return self.render_response('mills/upload_thanks.html')