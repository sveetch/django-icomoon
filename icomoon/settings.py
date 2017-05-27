"""
Default settings you can import your settings.py
"""
import os

# Define available webfonts
ICOMOON_WEBFONTS = {
    #'Default': {
        #'fontdir_path': 'static/fonts', # Where the font files belong and where they will be deployed
        #'csspart_path': 'static/css/icomoon_icons.scss', # Where the css part with all icon selectors will be written
    #},
}

# Private mode require to be logged to reach the gallery, use False to grant access
# to anonymous users
ICOMOON_PRIVATE = True

# Manifest filename, this is a Icomoon standard so you should not change it
ICOMOON_MANIFEST_FILENAME = "selection.json"

# Path to the CSS template that will contain icon map, this relative to templates directory
ICOMOON_CSS_TEMPLATE = "icomoon/icon_map.css"

# Structure and file requirements for the Icomoon webfont archive
# Also paths are relative within ZIP archive
ICOMOON_ARCHIVE_REQUIREMENT = {
    # Path where belong the font files
    'font_dir': 'fonts',
    # Allowed font format extensions
    'extensions': ['ttf', 'svg', 'eot', 'woff', 'woff2'],
}
