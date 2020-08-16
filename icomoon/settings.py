"""
Default settings to import in your settings file.
"""

ICOMOON_WEBFONTS = {}
"""
Define available webfonts
ICOMOON_WEBFONTS = {
    "Default": {
        # Where the font files belong and where they will be deployed
        "fontdir_path": "/home/foo/bar/static/fonts",
        # Where the css part with all icon selectors will be written
        "csspart_path": "/home/foo/bar/static/css/icomoon_icons.scss",
    },
}
"""

# Private mode require to be logged to reach the gallery, use False to grant
# access to anonymous users
ICOMOON_PRIVATE = True

# Manifest filename, this is a Icomoon standard so you should not change it
ICOMOON_MANIFEST_FILENAME = "selection.json"

# Path to the CSS template that will contain icon map, this relative to
# templates directory
ICOMOON_CSS_TEMPLATE = "icomoon/icon_map.css"
# Use this instead to create a Sass file with icon exposed as variables
# ICOMOON_CSS_TEMPLATE = "icomoon/icon_map.scss"

# Structure and file requirements for the Icomoon webfont archive
# Also paths are relative within ZIP archive
ICOMOON_ARCHIVE_REQUIREMENT = {
    # Path where belong the font files
    "font_dir": "fonts",
    # Allowed font format extensions
    "extensions": ["ttf", "svg", "eot", "woff", "woff2"],
}
