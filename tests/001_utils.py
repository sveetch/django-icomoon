import pytest

from icomoon.utils import IcomoonSettingsError, extend_webfont_settings


def test_extend_settings_success():
    """
    Correct settings, nothing to do
    """
    webfont_settings = {
        'fontdir_path': 'static/fonts',
        'csspart_path': 'static/css/icomoon_icons.scss',
    }
    result = extend_webfont_settings(webfont_settings)
    assert result == webfont_settings


@pytest.mark.parametrize('webfont_settings,attempted', [
    (
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': 'static/css/icomoon_icons.scss',
            'foo': True
        },
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': 'static/css/icomoon_icons.scss',
            'foo': True
        },
    ),
    (
        {
            'fontdir_path': 'static/fonts',
        },
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': None,
        },
    ),
    (
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': False,
        },
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': None,
        },
    ),
    (
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': '',
        },
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': None,
        },
    ),
    (
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': 0,
        },
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': None,
        },
    ),
    (
        {
            'fontdir_path': 'static/fonts',
            'foo': True
        },
        {
            'fontdir_path': 'static/fonts',
            'csspart_path': None,
            'foo': True
        },
    ),
])
def test_extend_settings_csspart_path(webfont_settings, attempted):
    """
    Missing or empty 'csspart_path' is automatically set to None
    """
    assert extend_webfont_settings(webfont_settings) == attempted


@pytest.mark.parametrize('webfont_settings', [
    {
        'csspart_path': 'static/css/icomoon_icons.scss',
    },
    {
        'fontdir_path': None,
        'csspart_path': 'static/css/icomoon_icons.scss',
    },
    {
        'fontdir_path': '',
        'csspart_path': 'static/css/icomoon_icons.scss',
    },
    {
        'fontdir_path': 0,
        'csspart_path': 'static/css/icomoon_icons.scss',
    },
    {
        'csspart_path': 'static/css/icomoon_icons.scss',
        'foo': True
    },
])
def test_extend_settings_fontdir_path(webfont_settings):
    """
    Missing or empty 'fontdir_path' lead to exception
    """
    with pytest.raises(IcomoonSettingsError):
        extend_webfont_settings(webfont_settings)
