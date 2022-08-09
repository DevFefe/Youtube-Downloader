import json
from pathlib import Path
from screeninfo import get_monitors

with open('../config.json', 'r') as f:
    config = json.load(f)

defaultDownloadPath = config['defaultDownloadPosition']

theme = config['theme']
defaultTheme = config['defaultTheme']
currentTheme = theme

resolution= config['resolution']
defaultResolution = config['defaultResolution']
currentResolution = resolution

WIDTH, HEIGTH = resolution

allResolutions = []

for monitor in get_monitors():
    monitorWidth = monitor.width
    monitorHeight = monitor.height

for res in config['allResolutions']:
    if res[0] < monitorWidth and res[1]< monitorHeight:
        allResolutions.append(res)

fontFamily = config['fontFamily']
fontSize = int(WIDTH/32)

def updateJSON(downloadPath, theme, resolution):
    global config
    config['downloadPosition'] = downloadPath
    config['theme'] = theme
    config['resolution'] = resolution
    with open('../config.json', 'w') as f:
        f.write(json.dumps(config))

def getDownloadPath():
    with open('../config.json', 'r') as f:
        config = json.load(f)

    return Path(config['downloadPosition'])