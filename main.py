from gui import *
from youtube import Link, Search
import webbrowser

def openSettings():
    s = Settings(g)

    while True:
        event, values = s.window.Read()

        if event == None:
            break
        if event == '-OK-':
            s.update(values)
            break
        if event == '-RESET-':
            s.reset()
            break
    s.window.close()

def openAbout():
    a = About()

    while True:
        event, values = a.window.Read()

        if event == None or event == '-EXIT-':
            break
        if event.startswith("URL "):
            url = event.split(' ')[1]
            webbrowser.open(url)
    a.window.close()

g = Gui()

while True:
    event, values = g.window.Read()

    if event == None:
        break
    if event == '-QUIT-':
        if sg.popup_yes_no('Sicuro di volere uscire', font=(fontFamily, int(fontSize/2)), keep_on_top=True) == 'Yes':
            break
    if event == '-SETTINGS-':
        openSettings()
    if event == '-ABOUT-':
        openAbout()
    if event == '-LINK_BUTTON-':
        g.clearGuiLink()
        link = Link(values['-LINK-'], g)
    if event == '-LINK_DOWNLOAD-':
        if values['VA'] == True:
            link.downloadVideoAndAudio()
        elif values['A'] == True:
            link.downloadAudio()
    if event == '-LINK_RESET-':
        g.resetGuiLink()
    if event == '-SEARCH_BUTTON-':
        g.clearGuiSearch()
        search = Search(values['-SEARCH-'], g)
    if event == '-SEARCH_TABLE-':
        search.getTableIndex(values[event])
    if event == '-SEARCH_DOWNLOAD-':
        if values['VA'] == True:
            search.downloadVideoAndAudio()
        elif values['A'] == True:
            search.downloadAudio()
    if event == '-SEARCH_RESET-':
        g.resetGuiSearch()
    
