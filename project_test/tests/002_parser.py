import os

import pytest

from icomoon.parser import WebfontStore


def test_parser(settings):
    """Parse basic webfont manifest"""
    store = WebfontStore('selection.json')

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


def test_get_manifest(settings):
    """TODO: Open and parse webfont manifest"""
    store = WebfontStore('selection.json')

    manifest_path = os.path.join(settings.TESTS_FIXTURES_DIR, 'icobasic_selection.json')

    webfont_name = "Default"


    webfont_settings = {
        'fontdir_path': 'static/fonts',
        'csspart_path': 'static/css/icomoon_icons.scss',
    }

    icon_map = store.get(webfont_name, webfont_settings)

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
