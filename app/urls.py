# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule
import apps.map.urls
import apps.collector.urls
import apps.admin.urls
import apps.mills.urls

rules = []
rules = rules +apps.map.urls.rules
rules = rules + apps.collector.urls.rules
rules = rules + apps.admin.urls.rules
rules = rules + apps.mills.urls.rules
