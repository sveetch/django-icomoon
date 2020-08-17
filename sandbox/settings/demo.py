"""
Django settings for demonstration

Intended to be used with ``make run``.
"""
from sandbox.settings.base import *

from icomoon.settings import *


ICOMOON_WEBFONTS = {
    'Default': {
        'fontdir_path': os.path.join(BASE_DIR, 'static/fonts'),
        'csspart_path': os.path.join(BASE_DIR, "static/css/icomoon_icons.scss"),
    },
}
