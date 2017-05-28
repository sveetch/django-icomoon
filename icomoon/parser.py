"""
Icomoon manifest parser
"""
import io
import os
import json
from collections import OrderedDict

from six import string_types

from icomoon.utils import IcomoonSettingsError, extend_webfont_settings


class WebfontStore(object):
    """
    Webfont store to collect every given manifest.

    Store assume every webfont manifest file are located inside their webfont
    directory set in their ``fontdir_path`` option.

    Store does not create any file, it just parse manifest and store icon maps.

    Manifest filename is the same for every webfont, it is given as
    ``WebfontStore`` init argument ``manifest_filename``, commonly
    ``selection.json``.

    Args:
        manifest_filename (string): Manifest filename to search for in webfont
            directory.
    """
    def __init__(self, manifest_filename):
        self.manifest_filename = manifest_filename
        self.manifests = OrderedDict()
        self.errors = {}

    def get_icon_key(self, elem):
        """
        Return the icon name to be used as a sorting key
        """
        return elem.get('properties').get('name')

    def parse_manifest(self, fp):
        """
        Open manifest JSON file and build icon map

        Args:
            fp (string or fileobject): Either manifest filepath to open or
                manifest File object.

        Returns:
            dict: Webfont icon map. Contains:

            * ``class_name``: Builded icon classname with prefix configured
              in manifest (from parameters in Icomoon interface);
            * ``int``: Icon integer code like ``59649``;
            * ``hex``: Icon hexadecimal code like ``0xe901``;
            * ``unicode``: Icon unicode like ``U+E901``;
            * ``utf8``! Icon UTF8 code like ``\e901``;
        """
        # Given a string for file path to open
        if isinstance(fp, string_types):
            fp = io.open(fp, 'r', encoding='utf-8')

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

    def get(self, webfont_name, webfont_settings):
        """
        Get a manifest file, parse and store it.

        Args:
            webfont_name (string): Webfont key name. Used to store manifest
                and potentially its parser error.
            webfont_settings (dict): Webfont settings (an item value from
                ``settings.ICOMOON_WEBFONTS``).
        """
        try:
            webfont_settings = extend_webfont_settings(webfont_settings)
        except IcomoonSettingsError as e:
            msg = "Invalid webfont settings for '{}': {}"
            self.errors[webfont_name] = msg.format(webfont_name, e.value)
            return

        filepath = os.path.join(webfont_settings['fontdir_path'],
                                self.manifest_filename)

        if os.path.exists(filepath):
            self.manifests[webfont_name] = self.parse_manifest(filepath)
        else:
            msg = ("""Filepath for webfont <strong>{name}</strong> does not """
                   """exists: <code>{filepath}</code>""")
            self.errors[webfont_name] = msg.format(name=webfont_name,
                                                   filepath=filepath)

    def fetch(self, webfonts):
        """
        Store every defined webfonts.

        Webfont are stored with sort on their name.

        Args:
            webfonts (dict): Dictionnary of webfont settings from
                ``settings.ICOMOON_WEBFONTS``.
        """
        sorted_keys = sorted(webfonts.keys())
        for webfont_name in sorted_keys:
            self.get(webfont_name, webfonts[webfont_name])

    def get_manifests(self):
        """
        Simple shortcut to get stored manifests.

        Returns:
            collections.OrderedDict: Stored webfont manifest.
        """
        return self.manifests
