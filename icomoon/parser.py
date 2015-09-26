"""
Icomoon manifest parser
"""
import json, os
from collections import OrderedDict
from operator import itemgetter


class WebfontStore(object):
    """
    Webfont store to collect every given manifest
    """
    def __init__(self, manifest_filepaths):
        self.manifests = OrderedDict()
        self.manifest_filepaths = manifest_filepaths
        self.errors = {}
        
        # Maintain compatibility for django-icomoon<0.2 installs when there was only an 
        # unique webfont without a name
        if isinstance(self.manifest_filepaths, basestring):
            self.manifest_filepaths = (('Default', self.manifest_filepaths),)
            
    def fetch(self):
        """
        Open all defined manifest files and parse them
        """
        sorted_manifests = sorted(self.manifest_filepaths, key=itemgetter(0))
        for name,filepath in sorted_manifests:
            if os.path.exists(filepath):
                self.manifests[name] = self.parse_manifest(filepath)
            else:
                self.errors[name] = "Filepath for webfont <strong>{name}</strong> does not exists: <code>{filepath}</code>".format(name=name, filepath=filepath)
            
    def get_icon_key(self, elem):
        """
        Return the icon name to be used as a sorting key
        """
        return elem.get('properties').get('name')

    def parse_manifest(self, fp):
        """
        Open the JSON file then find the icons and some options
        
        @fp is either a file object or a string containing the file path to open
        """
        # Given a string for file path to open
        if isinstance(fp, basestring):
            fp = open(fp, 'rb')
        
        with fp as json_file:
            webfont_manifest = json.load(json_file)
        
        # Get the font set prefix to know the css classname
        icon_prefix = webfont_manifest.get('preferences').get('fontPref').get('prefix')
        
        # Get sorted icons
        icons_map = OrderedDict()
        sorted_entries = sorted(webfont_manifest.get('icons'), key=self.get_icon_key)
        for icon_entry in sorted_entries:
            name = icon_entry.get('properties').get('name')
            code = icon_entry.get('properties').get('code')
            hexa_code = hex(code)

            icons_map[name] = {
                'class_name': icon_prefix + name,
                'int': code,
                'hex': hexa_code,
                'unicode': 'U+'+''.join(hex(code).split('x')[1:]).upper(),
                'utf8': '\\'+''.join(hex(code).split('x')[1:]).lower(),
            }
        
        return icons_map
            
    def get_manifests(self):
        return self.manifests
