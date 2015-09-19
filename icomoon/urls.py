# -*- coding: utf-8 -*-
"""
App URLs
"""
from django.conf.urls import *

from .views import WebfontIconListView

urlpatterns = patterns('',
    url(r'^$', WebfontIconListView.as_view(), name="index"),
)
