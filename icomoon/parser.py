"""
Icomoon manifest parser
"""
import json, os
from collections import OrderedDict
from operator import itemgetter

from icomoon.utils import IcomoonSettingsError, extend_webfont_settings

class WebfontStore(object):
    """
    Webfont store to collect every given manifest
    """
    def __init__(self, manifest_filename):
        self.manifest_filename = manifest_filename
        self.manifests = OrderedDict()
        self.errors = {}
            
    def fetch(self, webfonts):
        """
        Open all defined manifest files and parse them
        
        @webfonts: Dict of Dict from settings.ICOMOON_WEBFONTS
        """
        sorted_keys = sorted(webfonts.keys())
        for webfont_name in sorted_keys:
            self.get(webfont_name, webfonts[webfont_name])
            
    def get(self, webfont_name, webfont_settings):
        """
        Get a manifest file and parse it
        
        @webfont_name: Webfont key name
        @webfont_settings: Dict of webfont settings
        """
        try:
            webfont_settings = extend_webfont_settings(webfont_settings)
        except IcomoonSettingsError as e:
            self.errors[webfont_name] = "Invalid webfont settings for '{}': {}".format(webfont_name, e.value)
            return
            
        filepath = os.path.join(webfont_settings['fontdir_path'], self.manifest_filename)
        if os.path.exists(filepath):
            self.manifests[webfont_name] = self.parse_manifest(filepath)
        else:
            self.errors[webfont_name] = "Filepath for webfont <strong>{name}</strong> does not exists: <code>{filepath}</code>".format(name=webfont_name, filepath=filepath)
            
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
