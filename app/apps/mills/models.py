from google.appengine.ext import db, blobstore
from tipfy.appengine.db.properties import SlugProperty
from geo.geomodel import GeoModel

from BeautifulSoup import BeautifulSoup

import logging




class TagFactory(object):
    def __init__(self, steal_namespace_from):
        self.steal_namespace_from=steal_namespace_from

    def make_tag(self, new_tag):
        namespace=self.steal_namespace_from.tag[1:].split('}')[0]
        return "{%s}%s" % (namespace, new_tag)



class Mill(GeoModel):
	name = db.StringProperty()
	original_name=db.StringProperty()
	BuildDate=db.StringProperty()
	WaterSource=db.StringProperty()
	WaterShed=db.StringProperty()
	WheelType=db.StringProperty()
	WheelMaterial=db.StringProperty()
	WheelLocation=db.StringProperty()
	WheelCount=db.StringProperty()
	MillType=db.StringProperty()
	MillTypeSub=db.StringProperty()
	MillStatus=db.StringProperty()
	NearRoad=db.StringProperty()
	DataSource=db.StringProperty()
	Notes=db.StringProperty()
	slug=SlugProperty(name)
	mill_no=db.IntegerProperty()

	
	
	@classmethod
	def from_placemark(cls,placemark):
	    factory=TagFactory(placemark)
	    name_tag=factory.make_tag( "name")
	    description_tag=factory.make_tag("description")
	    point_tag=factory.make_tag("Point")
	    coords_tag=factory.make_tag("coordinates")
	    
	    name=placemark.find(name_tag).text
	    description=placemark.find(description_tag).text
	    point=placemark.find(point_tag)
	    coords_str=point.find(coords_tag).text
	    soup=BeautifulSoup(description)
	    outertable=soup.find('table')
	    innertable=outertable.find('table')
	    data= dict([(tr.findAll('td')[0].text, tr.findAll('td')[1].text) for tr in innertable.findAll('tr')])
	    lon, lat=[float(num) for num in coords_str.split(',')]
	    
	    new_mill=cls(name=name,
	                original_name=data.get('NameOriginal'),
	                BuildDate=data.get("BuildDate"),
	                	WaterSource=data.get("WaterSource"),
                        WaterShed=data.get("WaterShed"),
                        WheelType=data.get("WheelType"),
                        WheelMaterial=data.get("WheelMaterial"),
                        WheelLocation=data.get("WheelLocation"),
                        WheelCount=data.get("WheelCount"),
                        MillType=data.get("MillType"),
                        MillTypeSub=data.get("MillTypeSub"),
                        MillStatus=data.get("MillStatus"),
                        NearRoad=data.get("NearRoad"),
                        DataSource=data.get("DataSource"),
                        Notes=data.get("Notes"),
                        mill_no=int(data.get("MillId")),
                        key_name=data.get("MillId"),
                        location = db.GeoPt(lat, lon)
                        )
	    new_mill.update_location()
	    new_mill.put()
	                


