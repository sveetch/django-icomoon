import os
import shutil

import pytest

from icomoon.parser import WebfontStore


# Attempted map from 'icobasic_selection.json' sample manifest
ICOBASIC_MAP = {
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


def test_parser(settings):
    """Parse basic webfont manifest"""
    store = WebfontStore('selection.json')

    manifest_path = os.path.join(settings.TESTS_FIXTURES_DIR,
                                 'icobasic_selection.json')

    icon_map = store.parse_manifest(manifest_path)

    assert icon_map == ICOBASIC_MAP


@pytest.mark.parametrize('webfont_name,webfont_settings,error', [
    (
        'Foo',
        {
            'csspart_path': 'static/css/icomoon_icons.scss',
        },
        ("""Invalid webfont settings for 'Foo': Webfont settings miss the """
            """required key item 'fontdir_path'"""),
    ),
    (
        'Bar',
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': 'static/css/icomoon_icons.scss',
        },
        ("""Filepath for webfont <strong>Bar</strong> does not exists: """
            """<code>static/fonts/selection.json</code>"""),
    ),
])
def test_get_manifest_error(webfont_name, webfont_settings, error):
    """Fail to get given webfont"""
    store = WebfontStore('selection.json')

    icon_map = store.get(webfont_name, webfont_settings)

    assert store.errors[webfont_name] == error


def test_get_manifest_success(settings, temp_builds_dir):
    """TODO: Open and parse webfont manifest"""
    basedir = temp_builds_dir.join('get_manifest_success').strpath
    os.makedirs(basedir)

    shutil.copy(
        os.path.join(settings.TESTS_FIXTURES_DIR,
                     'icobasic_selection.json'),
        os.path.join(basedir,
                     'icobasic_selection.json'),
    )

    store = WebfontStore('icobasic_selection.json')

    store.get("Foo", {
        'fontdir_path': basedir,
        'csspart_path': 'static/css/foo.scss',
    })

    assert 'Foo' in store.get_manifests()

    assert store.get_manifests()['Foo'] == ICOBASIC_MAP
