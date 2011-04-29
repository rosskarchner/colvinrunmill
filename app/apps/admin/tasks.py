from google.appengine.ext import db, blobstore
from google.appengine.api.taskqueue import Task
from tipfy import RequestHandler, Response
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






class ImportKMLLayer(RequestHandler):
    def post(self):
        layer=self.request.form['layer']
        kml_id=self.request.form['kml_id']
        br=blobstore.BlobReader(kml_id)
        kml=extract_kml(br)
        et = ElementTree(file=kml)
        root=et.getroot()
        kml_namespace=root.tag[1:].split('}')[0]
        folder_tag="{%s}Folder" % kml_namespace
        name_tag="{%s}name" % kml_namespace
        placemark_tag="{%s}Placemark" % kml_namespace
        for document in list(root):
            for folder in document.findall(folder_tag):
                if folder.attrib['id'] != layer: continue
                mills=folder.findall(placemark_tag)
                logging.warning(mills)
                for mill in mills:
                    Mill.from_placemark(mill)
                
        return("OK")