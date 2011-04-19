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
    Rule('/collector/', endpoint='collector', handler='apps.collector.handlers.InputCollector'),
    Rule('/collector/thanks/', endpoint='collector-thanks', handler='apps.collector.handlers.ThanksHandler'),
    
]

