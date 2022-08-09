import json
from pathlib import Path
import os
from screeninfo import get_monitors
import PySimpleGUI as sg

with open('./config.json', 'r') as f:
    config = json.load(f)

defaultDownloadPath = ''

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

if config['downloadPosition'] == '':
    sg.theme(theme)
    folder = None
    while True:
        folder = sg.PopupGetFolder('Selezione cartella per download', font=(fontFamily, int(fontSize/2)))
        if folder == '':
            sg.Popup('Inserire una cartella', font=(fontFamily, int(fontSize/2)))
        elif not os.path.exists(folder):
            sg.Popup('Cartella inesistente, riprovare!', font=(fontFamily, int(fontSize/2)))
        else:
            break

    config['downloadPosition'] = folder
    config['defaultDownloadPosition'], defaultDownloadPath = folder, folder

    with open('./config.json', 'w') as f:
        f.write(json.dumps(config))

def updateJSON(downloadPath, theme, resolution):
    global config
    if downloadPath == '':
        sg.Popup('Inserire una cartella', font=(fontFamily, int(fontSize/2)), keep_on_top=True)
    elif not os.path.exists(downloadPath):
        sg.Popup('Cartella inesistente, riprovare!', font=(fontFamily, int(fontSize/2)), keep_on_top=True)
    else:
        config['downloadPosition'] = downloadPath
    config['theme'] = theme
    config['resolution'] = resolution
    with open('./config.json', 'w') as f:
        f.write(json.dumps(config))

def getDownloadPath():
    with open('./config.json', 'r') as f:
        config = json.load(f)

    return Path(config['downloadPosition'])
