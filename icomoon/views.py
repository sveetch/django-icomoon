# -*- coding: utf-8 -*-
"""
App views
"""
import json, os

#from django.db import models
from django.conf import settings
from django.views import generic

from braces.views import LoginRequiredMixin

from .parser import parse_icomoon_manifest

"../../project/webapp_statics/fonts/selection.json"
#manifest = parse_icomoon_manifest(open(MAP_FILEPATH, 'rb'))
#print json.dumps(manifest, indent=4)

class WebfontIconListView(LoginRequiredMixin, generic.TemplateView):
    """
    View listing icon getted from Icomoon manifest
    """
    template_name = "icomoon/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(WebfontIconListView, self).get_context_data(**kwargs)
        manifest_filepath = getattr(settings, 'ICOMOON_MANIFEST_FILEPATH', None)
        context.update({
            'ICOMOON_MANIFEST_FILEPATH': manifest_filepath,
            'icomoon_manifest': None,
        })
        
        if manifest_filepath and os.path.exists(manifest_filepath):
            context['icomoon_manifest'] = parse_icomoon_manifest(open(manifest_filepath, 'rb'))
        return context
