# -*- coding: utf-8 -*-
"""
App URLs
"""
from django.urls import path

from icomoon.views import WebfontIconListView

app_name = 'icomoon'

urlpatterns = [
    path('', WebfontIconListView.as_view(), name="index"),
]
