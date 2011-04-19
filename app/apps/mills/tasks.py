import logging

from google.appengine.ext import db, blobstore

from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from apps.mills.models import Mill


class SaveOrUpdateMillTask(RequestHandler):
    def post(self):
    	logging.info(str(self.request.form))
    	mill=Mill(key_name=self.request.form['MILL_NO'], 
    	name=self.request.form['MILL_NAME'],
    	location=db.GeoPt(float(self.request.form['Lat']), float(self.request.form['Long'])),
    	)
    	mill.mill_no=int(self.request.form['MILL_NO'])
    	mill.year=self.request.form['YEAR']
 
    	mill.update_location()
    	mill.put()
    	
        return Response()
