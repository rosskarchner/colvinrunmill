# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE.txt for more details.
"""
from tipfy import Rule



"""Returns a list of URL rules for the Hello, World! application.

:param app:
    The WSGI application instance.
:return:
    A list of class:`tipfy.Rule` instances.
"""
rules = [
    Rule('/admin/', endpoint='admin/index', handler='apps.admin.handlers.IndexHandler'),
    Rule('/admin/save-photo', endpoint='admin/save-photo', handler='apps.admin.handlers.SavePhotoHandler'),
    Rule('/admin/uploadkml', endpoint='admin/uploadkml', handler='apps.admin.handlers.UploadKMLHandler'),
    Rule('/admin/select-layer/<kml_id>/',endpoint='admin/selectlayer',handler='apps.admin.handlers.SelectLayerHandler')
]


