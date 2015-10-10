class IcomoonSettingsError(Exception):
    """Exception to raise when the settings are invalid"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def extend_webfont_settings(webfont_settings):
    """
    Should valid webfont settings, fill missing optional key then 
    return them
    """
    if 'fontdir_path' not in webfont_settings:
        raise IcomoonSettingsError("Webfont settings miss the required key item 'fontdir_path'")
    if 'csspart_path' not in webfont_settings:
        webfont_settings['csspart_path'] = None
    
    return webfont_settings
