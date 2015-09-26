# -*- coding: utf-8 -*-
"""
App views
"""
import json, os

#from django.db import models
from django.conf import settings
from django.views import generic

from .parser import WebfontStore


class WebfontIconListFreeView(generic.TemplateView):
    """
    View listing icon getted from Icomoon manifest
    """
    template_name = "icomoon/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(WebfontIconListFreeView, self).get_context_data(**kwargs)
        
        manifest_filepath = getattr(settings, 'ICOMOON_MANIFEST_FILEPATH', None)
        if manifest_filepath is not None:
            webfont_store = WebfontStore(manifest_filepath)
            webfont_store.fetch()
            context['webfont_store'] = webfont_store
            
        return context

if getattr(settings, 'ICOMOON_PRIVATE', True):
    from braces.views import LoginRequiredMixin
    
    class WebfontIconListView(LoginRequiredMixin, WebfontIconListFreeView):
        pass
else:
    class WebfontIconListView(WebfontIconListFreeView):
        pass
