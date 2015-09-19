"""
Icomoon manifest parser
"""
import json

def parse_icomoon_manifest(fp):
    """
    Just open the JSON file then find the icons and some options
    """
    with fp as json_file:
        webfont_manifest = json.load(json_file)

    #print webfont_manifest
    icon_prefix = webfont_manifest.get('preferences').get('fontPref').get('prefix')

    icons_map = {}
    for icon_entry in webfont_manifest.get('icons'):
        name = icon_entry.get('properties').get('name')
        code = icon_entry.get('properties').get('code')
        hexa_code = hex(code)
        #print code
        #print hexa_code
        #print 'U+'+''.join(hex(code).split('x')[1:]).upper()
        #print

        icons_map[name] = {
            'class_name': icon_prefix + name,
            'int': code,
            'hex': hexa_code,
            'unicode': 'U+'+''.join(hex(code).split('x')[1:]).upper(),
            'utf8': '\\'+''.join(hex(code).split('x')[1:]).lower(),
        }
    
    return icons_map

#MAP_FILEPATH = "../../project/webapp_statics/fonts/selection.json"
#manifest = parse_icomoon_manifest(open(MAP_FILEPATH, 'rb'))
#print json.dumps(manifest, indent=4)