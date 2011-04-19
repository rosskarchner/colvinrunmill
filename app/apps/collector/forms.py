from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin
from tipfyext.wtforms import Form, fields, validators, widgets
from tipfyext.wtforms.validators import ValidationError



REQUIRED=validators.required()

class AddPhotoForm(Form):
	image = fields.FileField(u'Add an Image', )
	name= fields.TextField('Your name', validators=[REQUIRED,])
	email=fields.TextField('Email',validators=[REQUIRED,] )
	phone=fields.TextField('Phone', )
	lat=fields.FloatField(' ', widget=widgets.HiddenInput())
	lon=fields.FloatField(' ', widget=widgets.HiddenInput())
	existing_photo=fields.HiddenField(' ')