import PySimpleGUI as sg
from layouts import MAIN_WINDOW_LAYOUT
from config import *

class Gui:
    def __init__(self):
        self.window = sg.Window('Youtube Downloader', MAIN_WINDOW_LAYOUT)

    def showGuiLink(self):
        self.window['-LINK_IMAGE-'].update(visible=True)
        self.window['-LINK_INFO-'].update(visible=True)
        self.window['-LINK_DOWNLOAD-'].update(visible=True)
        self.window['-LINK_RESET-'].update(visible=True)
        self.window['-LINK_PROGRESSBAR-'].update(visible=True)

    def clearGuiLink(self):
        self.window['-LINK_IMAGE-'].update(visible=False)
        self.window['-LINK_INFO-'].update(visible=False)
        self.window['-LINK_DOWNLOAD-'].update(visible=False)
        self.window['-LINK_RESET-'].update(visible=False)
        self.window['-LINK_PROGRESSBAR-'].update(visible=False)

    def resetGuiLink(self):
        self.window['-LINK-'].update(value='')
        self.window['-LINK_IMAGE-'].update(visible=False)
        self.window['-LINK_INFO-'].update(visible=False)
        self.window['-LINK_DOWNLOAD-'].update(visible=False)
        self.window['-LINK_RESET-'].update(visible=False)
        self.window['-LINK_PROGRESSBAR-'].update(visible=False)

    def showGuiSearch(self):
        self.window['-SEARCH_TABLE-'].update(visible=True)
        self.window['-SEARCH_RESET-'].update(visible=True)

    def clearGuiSearch(self):
        self.window['-SEARCH_TABLE-'].update(values=[])
        self.window['-SEARCH_TABLE-'].update(visible=False)
        self.window['-SEARCH_DOWNLOAD-'].update(visible=False)
        self.window['-SEARCH_RESET-'].update(visible=False)
        self.window['-SEARCH_PROGRESSBAR-'].update(visible=False)

    def resetGuiSearch(self):
        self.window['-SEARCH-'].update(value='')
        self.window['-SEARCH_TABLE-'].update(values=[])
        self.window['-SEARCH_TABLE-'].update(visible=False)
        self.window['-SEARCH_DOWNLOAD-'].update(visible=False)
        self.window['-SEARCH_RESET-'].update(visible=False)
        self.window['-SEARCH_PROGRESSBAR-'].update(visible=False)

class Settings:
    def __init__(self, mainWindow):
        SETTINGS_LAYOUT = [
            [
                sg.Frame('', [
                        [
                            sg.Text('Folder', font=(fontFamily, int(fontSize/2))),
                            sg.In(getDownloadPath(), size=(25,1), enable_events=True ,key='-FOLDER-', font=(fontFamily, int(fontSize/2))),
                            sg.FolderBrowse(font=(fontFamily, int(fontSize/2)), key='-FOLDER_BUTTON-')
                        ],
                        [
                            sg.Text('Theme', font=(fontFamily, int(fontSize/2))),
                            sg.Combo(sg.theme_list(), default_value=theme, key='-THEME-', font=(fontFamily, int(fontSize/2)))
                        ],
                        [
                            sg.Text('Risoluzione', font=(fontFamily, int(fontSize/2))),
                            sg.Combo(allResolutions, default_value=resolution, key='-RES-', font=(fontFamily, int(fontSize/2)))
                        ],
                        [
                            sg.Button("Reset", expand_x=True, key='-RESET-', font=(fontFamily, int(fontSize/2))),
                            sg.Button("Ok", expand_x=True, key='-OK-', font=(fontFamily, int(fontSize/2)))
                        ]
                    ],
                    border_width=0
                )
            ]
        ]
        
        self.window = sg.Window('Settings', SETTINGS_LAYOUT, keep_on_top=True)

        self.mainWindow = mainWindow

    def update(self, values):
        self.window['-FOLDER-'].update(disabled=True)
        self.window['-FOLDER_BUTTON-'].update(disabled=True)
        self.window['-THEME-'].update(disabled=True)
        self.window['-RES-'].update(disabled=True)

        updateJSON(values['-FOLDER-'], values['-THEME-'], values['-RES-'])
        if values['-THEME-'] != currentTheme or values['-RES-'] != currentResolution:
            self.restartPopUp()


    def reset(self):
        downloadPath = defaultDownloadPath
        theme = defaultTheme
        resolution = defaultResolution
        updateJSON(downloadPath, theme, resolution)
        if theme != currentTheme or resolution != currentResolution:
            self.restartPopUp()

    def restartPopUp(self):
        if sg.popup_yes_no('Riavvio necessario per applicare cambiamenti\nRiavviare ora?', font=(fontFamily, int(fontSize/2)), keep_on_top=True) == 'Yes':
            self.mainWindow.window.close()

class About:
    def __init__(self):
        SETTINGS_LAYOUT = [
            [
                sg.Text('Sviluppatore: Federico Lisio\nEmail: federico.lisio.05@gmail.com', font=(fontFamily, int(fontSize/2))),
            ],
            [
                sg.Text('GitHub', tooltip='https://github.com/DevFefe', enable_events=True, font=(fontFamily, str(int(int(fontSize/2))), 'underline'), key='URL https://github.com/DevFefe')
            ],
            [
                sg.Button("Chiudi", expand_x=True, key='-EXIT-', font=(fontFamily, int(fontSize/2)))
            ]
        ]
        
        self.window = sg.Window('Settings', SETTINGS_LAYOUT, keep_on_top=True)

class Download():
    def __init__(self):
        DOWNLOAD_LAYOUT = [
            [
                sg.Text('Download Completato!', font=(fontFamily, int(fontSize/2)))
            ],
            [
                sg.Button('Ok', key='-CLOSE-', font=(fontFamily, int(fontSize/2)), expand_x=True),
                sg.Button('Apri nella cartella', key='-OPEN_FOLDER-', font=(fontFamily, int(fontSize/2)), expand_x=True)
            ]
        ]

        self.window = sg.Window('Download Complete', DOWNLOAD_LAYOUT, keep_on_top=True)