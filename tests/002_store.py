import os
import shutil

import pytest

from icomoon.store import WebfontStore


# Attempted map from 'icobasic/selection.json' sample manifest
ICOBASIC_MAP = {
    "heart": {
        "class_name": "iconbasic-heart",
        "hex": "0xe900",
        "int": 59648,
        "unicode": "U+E900",
        "utf8": "\\e900"
    },
    "star": {
        "class_name": "iconbasic-star",
        "hex": "0xe901",
        "int": 59649,
        "unicode": "U+E901",
        "utf8": "\\e901"
    }
}


# Attempted map from 'icomoon/selection.json' sample manifest
ICOMOON_MAP = {
    "minus-alt": {
        "class_name": "icon-minus-alt",
        "int": 59649,
        "hex": "0xe901",
        "unicode": "U+E901",
        "utf8": "\\e901"
    },
    "arrow-up": {
        "class_name": "icon-arrow-up",
        "int": 59954,
        "hex": "0xea32",
        "unicode": "U+EA32",
        "utf8": "\\ea32"
    },
    "arrow-left": {
        "class_name": "icon-arrow-left",
        "int": 59960,
        "hex": "0xea38",
        "unicode": "U+EA38",
        "utf8": "\\ea38"
    },
    "arrow-right": {
        "class_name": "icon-arrow-right",
        "int": 59956,
        "hex": "0xea34",
        "unicode": "U+EA34",
        "utf8": "\\ea34"
    },
    "map-pin-fill": {
        "class_name": "icon-map-pin-fill",
        "int": 59650,
        "hex": "0xe902",
        "unicode": "U+E902",
        "utf8": "\\e902"
    },
    "home": {
        "class_name": "icon-home",
        "int": 59651,
        "hex": "0xe903",
        "unicode": "U+E903",
        "utf8": "\\e903"
    },
    "plus-alt": {
        "class_name": "icon-plus-alt",
        "int": 59648,
        "hex": "0xe900",
        "unicode": "U+E900",
        "utf8": "\\e900"
    },
    "arrow-down": {
        "class_name": "icon-arrow-down",
        "int": 59958,
        "hex": "0xea36",
        "unicode": "U+EA36",
        "utf8": "\\ea36"
    }
}


def test_parser(tests_settings):
    """
    Parse basic webfont manifest
    """
    store = WebfontStore("selection.json")

    manifest_path = tests_settings.fixtures_path / "icobasic" / "selection.json"

    icon_map = store.parse_manifest(manifest_path)

    assert icon_map == ICOBASIC_MAP


@pytest.mark.parametrize('webfont_name,webfont_settings,error', [
    (
        "Foo",
        {
            "csspart_path": "static/css/icomoon_icons.scss",
        },
        ("""Invalid webfont settings for 'Foo': Webfont settings miss the """
            """required key item 'fontdir_path'"""),
    ),
    (
        "Bar",
        {
            "fontdir_path": "static/fonts",
            "csspart_path": "static/css/icomoon_icons.scss",
        },
        ("""Filepath for webfont <strong>Bar</strong> does not exists: """
            """<code>static/fonts/selection.json</code>"""),
    ),
])
def test_get_manifest_error(webfont_name, webfont_settings, error):
    """
    Fail to get given webfont
    """
    store = WebfontStore("selection.json")

    store.get(webfont_name, webfont_settings)

    assert store.errors[webfont_name] == error


def test_get_manifest_success(tests_settings, tmp_path):
    """
    Succeed to get given webfont
    """
    # Install icobasic webfont in temporary dir
    icobasic_path = os.path.join(tmp_path, "icobasic")
    os.makedirs(icobasic_path)
    shutil.copy(
        os.path.join(tests_settings.fixtures_path, "icobasic",
                     "selection.json"),
        os.path.join(icobasic_path, "selection.json"),
    )

    store = WebfontStore("selection.json")

    store.get("Foo", {
        "fontdir_path": icobasic_path,
        "csspart_path": "static/css/foo.scss",
    })

    assert "Foo" in store.get_manifests()

    assert store.get_manifests()["Foo"] == ICOBASIC_MAP


def test_fetch(tests_settings, tmp_path):
    """
    Fetching all webfonts
    """
    # Install icobasic webfont in temporary dir
    icobasic_path = tmp_path / "icobasic"
    icobasic_path.mkdir()
    shutil.copy(
        tests_settings.fixtures_path / "icobasic" / "selection.json",
        icobasic_path / "selection.json",
    )

    # Install icomoon webfont in temporary dir
    icomoon_path = tmp_path / "icomoon"
    icomoon_path.mkdir()
    shutil.copy(
        tests_settings.fixtures_path / "icomoon" / "selection.json",
        icomoon_path / "selection.json",
    )

    store = WebfontStore("selection.json")

    store.fetch({
        "Foo": {
            "fontdir_path": icobasic_path,
            "csspart_path": "static/css/foo.scss",
        },
        "Bar": {
            "fontdir_path": icomoon_path,
            "csspart_path": "static/css/bar.scss",
        },
    })

    assert "Foo" in store.get_manifests()
    assert "Bar" in store.get_manifests()

    assert store.get_manifests()["Foo"] == ICOBASIC_MAP
    assert store.get_manifests()["Bar"] == ICOMOON_MAP
