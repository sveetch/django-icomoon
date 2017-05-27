import os

import pytest

from icomoon.parser import WebfontStore


def test_parser(settings):
    """Parse basic webfont manifest"""
    store = WebfontStore('Basic')

    manifest_path = os.path.join(settings.TESTS_FIXTURES_DIR, 'icobasic_selection.json')

    icon_map = store.parse_manifest(manifest_path)

    assert icon_map == {
        'heart': {
            'class_name': 'iconbasic-heart',
            'hex': '0xe900',
            'int': 59648,
            'unicode': 'U+E900',
            'utf8': '\\e900'
        },
        'star': {
            'class_name': 'iconbasic-star',
            'hex': '0xe901',
            'int': 59649,
            'unicode': 'U+E901',
            'utf8': '\\e901'
        }
    }
