"""
Django settings for tests
"""
from sandbox.settings.base import *

DATABASES = {
    # Development default database engine use sqlite3
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db', 'tests.sqlite3'),
        'TEST': {
            'NAME': os.path.join(DATA_DIR, 'db', 'tests.sqlite3'),  # noqa
        }
    }
}

# Absolute filesystem path to the directory that contain tests fixtures files
TESTS_FIXTURES_DIR = os.path.join('..', 'tests', 'data_fixtures')

# Media directory dedicated to tests
MEDIA_ROOT = os.path.join(DATA_DIR, "media-tests")

from icomoon.settings import *
