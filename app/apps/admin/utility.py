from zipfile import ZipFile

from StringIO import StringIO

def extract_kml(br):
        if ".kmz" in  br.blob_info.content_type:
            kmz=ZipFile(br)
            #import pdb;pdb.set_trace()
            kml_file_name=""
            for name in kmz.namelist():
                if ".kml" in name: kml_file_name=name
            kml= StringIO(kmz.read(kml_file_name) )
        elif ".kml" in  br.blob_info.content_type:
            kml=br
        
        return kml