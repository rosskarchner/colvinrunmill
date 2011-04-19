
from tipfyext.wtforms import Form, fields, validators, widgets
from tipfyext.wtforms.validators import ValidationError



REQUIRED=validators.required()

class UploadKMLForm(Form):
	kml = fields.FileField(u'Upload a new Mills KML', validators=[REQUIRED,])
	