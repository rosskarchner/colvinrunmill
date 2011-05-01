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
    Rule('/tasks/update-mill', endpoint='tasks/update-mill', handler='apps.mills.tasks.SaveOrUpdateMillTask'),
    Rule('/mills.json', endpoint='mills/js', handler='apps.mills.handlers.MarkersJS'),
    Rule('/mills/<mill_no>/<slug>', endpoint='mills/single', handler='apps.mills.handlers.MillPage'),
    Rule('/mills/<mill_no>/<slug>/add-photo', endpoint='mills/addphoto', handler='apps.mills.handlers.AddPhoto'),
    Rule('/mills/thanks', endpoint="photo-upload-thanks", handler='apps.mills.handlers.PhotoUploadThanks')
]

