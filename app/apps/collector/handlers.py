# -*- coding: utf-8 -*-

from google.appengine.ext import db, blobstore

from werkzeug import MultiDict, cached_property

from tipfy.appengine.db import get_entity_dict
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin
from tipfy.appengine.blobstore import BlobstoreUploadMixin


from forms import AddPhotoForm
from models import Photo


class InputCollector(RequestHandler, Jinja2Mixin, BlobstoreUploadMixin):
    def get(self):
        upload_url = blobstore.create_upload_url(self.url_for('collector'))
        return self.render_response('collector/collect.html', form=self.form, upload_url=upload_url)


    def post(self):
        if self.get_uploads('image'):
            upload_files = self.get_uploads('image')
            blob_info = upload_files[0]
            
        else:
            blob_info=None
            
        if self.form.validate():
            form=self.form
            photo=Photo(name=form.name.data,
            image=blob_info
            )
            
            if (form.lat.data and form.lon.data):
                photo.location=db.GeoPt(lat=form.lat.data,lon= form.lon.data)
            
            photo.put()
            response = redirect_to('collector-thanks',)
            
        else:
			form=self.form
			photo=Photo(name=form.name.data,
			email=form.email.data,
			phone=form.phone.data,
			image=blob_info
			)

			photo.put()
			response = redirect_to('collector',photo=photo.key())
            
            
        # Clear the response body.
        response.data = ''
        return response

    @cached_property
    def form(self):
        if self.request.args.get('photo'):
            key=db.Key(self.request.args['photo'])
            photo=Photo.get(key)
            form_data=MultiDict({
                'name':photo.name,
                'existing_photo':key,
                'email':photo.email,
                'phone':photo.phone,

            
            
            }.iteritems())
            
            
            return(AddPhotoForm(form_data))
            
        else:
            return AddPhotoForm(self.request.form)
        

class ThanksHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('collector/thanks.html')
        
