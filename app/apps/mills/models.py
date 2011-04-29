from google.appengine.ext import db, blobstore
from tipfy.appengine.db.properties import SlugProperty
from geo.geomodel import GeoModel

from BeautifulSoup import BeautifulSoup

import logging



def filter_null(value):
    if "Null" in value: return None
    return value


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
	                original_name=filter_null(data.get('NameOriginal')),
	                BuildDate=filter_null(data.get("BuildDate")),
	                	WaterSource=filter_null(data.get("WaterSource")),
                        WaterShed=filter_null(data.get("WaterShed")),
                        WheelType=filter_null(data.get("WheelType")),
                        WheelMaterial=filter_null(data.get("WheelMaterial")),
                        WheelLocation=filter_null(data.get("WheelLocation")),
                        WheelCount=filter_null(data.get("WheelCount")),
                        MillType=filter_null(data.get("MillType")),
                        MillTypeSub=filter_null(data.get("MillTypeSub")),
                        MillStatus=filter_null(data.get("MillStatus")),
                        NearRoad=filter_null(data.get("NearRoad")),
                        DataSource=filter_null(data.get("DataSource")),
                        Notes=filter_null(data.get("Notes")),
                        mill_no=int(data.get("MillId")),
                        key_name=data.get("MillId"),
                        location = db.GeoPt(lat, lon)
                        )
	    new_mill.update_location()
	    new_mill.put()
	                


