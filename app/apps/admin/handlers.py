import logging
from google.appengine.api.labs import taskqueue
from google.appengine.ext import db, blobstore

from werkzeug import cached_property
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from forms import UploadKMLForm

from csv import DictReader

from apps.collector.models import Photo
from apps.mills.models import Mill
from tipfy.appengine.blobstore import BlobstoreUploadMixin

from zipfile import ZipFile

from xml.etree.ElementTree import ElementTree

from StringIO import StringIO

from utility import extract_kml

class IndexHandler(RequestHandler, Jinja2Mixin):
    def get(self):
    	upload_url = blobstore.create_upload_url(self.url_for('admin/uploadkml'))
    	#upload_url = self.url_for('admin/uploadkml')
    	mills= Mill.all().fetch(1000)

    	#return self.render_response('admin.html')
    	return self.render_response('admin.html', 
    	    upload_kml_form=self.upload_kml_form,
    	    upload_url=upload_url,
    	    )
    	

    @cached_property
    def upload_kml_form(self):
        return UploadKMLForm()



class UploadKMLHandler(RequestHandler, BlobstoreUploadMixin):
    @cached_property
    def form(self):
    	
        return UploadKMLForm(self.request.form)
        
        
    def post(self):
    	milldata=self.get_uploads('kml')[0]
    	logging.warning('/admin/select-layer/%s/'% str(milldata.key()))
    	
        response= self.redirect('/admin/select-layer/%s/'% str(milldata.key()), 302)
        response.data = ''
        return response

        	
class SelectLayerHandler(RequestHandler, Jinja2Mixin):
    def get(self, kml_id):
        br=blobstore.BlobReader(kml_id)
        kml=extract_kml(br)
        et = ElementTree(file=kml)
        root=et.getroot()
        kml_namespace=root.tag[1:].split('}')[0]
        folder_tag="{%s}Folder" % kml_namespace
        name_tag="{%s}name" % kml_namespace
        folders=[]
        for document in list(root):
            for folder in document.findall(folder_tag):
                name=folder.find(name_tag).text
                if name: 
                    logging.warning('found folder %s',name)
                    folders.append([folder.attrib['id'],name])
        
        return self.render_response('select_layer.html', 
    	    folders=folders,
    	    )

    def post(self,kml_id):
        importer=taskqueue.Task(url='/tasks/import_kml_layer',
                      params={'kml_id':kml_id,
                              'layer':self.request.form['layer']})
        importer.add()
        return "thanks!"

            
            