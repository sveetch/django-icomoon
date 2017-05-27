class IcomoonSettingsError(Exception):
    """Exception to raise when settings are invalid"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def extend_webfont_settings(webfont_settings):
    """
    Valid webfont settings, fill missing optional key then return them
    """
    if not webfont_settings.get('fontdir_path', False):
        raise IcomoonSettingsError("Webfont settings miss the required key item 'fontdir_path'")
    if not webfont_settings.get('csspart_path', False):
        webfont_settings['csspart_path'] = None

    return webfont_settings
