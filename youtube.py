import PySimpleGUI as sg
import pytube, io, os, platform
from PIL import Image
from support import *
from config import *
from gui import Download

from pytube.cli import on_progress

class Link():
    def __init__(self, link, gui):

        self.window = gui.window

        try:
            self.yt = pytube.YouTube(link, on_progress_callback=self.progressFunction, on_complete_callback=self.completeFunction)

            self.title = self.yt.title
            self.length = getVideoLength(self.yt.length)
            self.videoAndAudioSize = getVideoSize(self.yt.streams.get_highest_resolution().filesize)
            self.audioSize = getVideoSize(self.yt.streams.get_audio_only().filesize)

            getVideoThumbnail(self.yt.thumbnail_url)

            self.updateGui()
            gui.showGuiLink()

        except pytube.exceptions.PytubeError:
            errorPopUp('Link errato')
            gui.clearGuiLink()

        except:
            errorPopUp('Errore riscontrato, provare a:\n- Controllare Connessione\n- Riavviare app\n- Contattare sviluppatore')
            gui.clearGuiLink()

    def updateGui(self):
        image = Image.open('./image.png')
        image.thumbnail((int(WIDTH/100*40), int(HEIGTH/100*40)))
        bio = io.BytesIO()
        image.save(bio, format='PNG')
        self.window['-LINK_IMAGE-'].update(data=bio.getvalue())

        os.remove('./image.png')

        self.window['-LINK_TITLE-'].update(value=self.title)
        self.window['-LINK_VIDEO_LENGTH-'].update(value=self.length)
        self.window['-LINK_VIDEO_AND_AUDIO_SIZE-'].update(value=self.videoAndAudioSize)
        self.window['-LINK_AUDIO_SIZE-'].update(value=self.audioSize)

    def downloadVideoAndAudio(self):
        try:
            self.yt.streams.get_highest_resolution().download(getDownloadPath())
        except:
            errorPopUp('Errore durante il download')

    def downloadAudio(self):
        try:
            self.yt.streams.get_audio_only().download(getDownloadPath())
        except:
            errorPopUp('Errore durante il download')

    def progressFunction(self, stream, chunk, bytes_remaining):
        current = ((stream.filesize - bytes_remaining)/stream.filesize)
        percent = current*100

        self.window['-LINK_PROGRESSBAR-'].update(percent)

    def completeFunction(stream, file_path, self):
        d = Download()

        while True:
            event, values = d.window.Read()

            if event == None or event == '-CLOSE-':
                break
            if event == '-OPEN_FOLDER-':
                match platform.system():
                    case 'Darwin':
                        os.system(f'open {os.path.realpath(getDownloadPath())}')
                    case 'Linux':
                        os.system(f'open {os.path.realpath(getDownloadPath())}')
                    case 'Window':
                        os.system(f'start {os.path.realpath(getDownloadPath())}')

        d.window.close()

class Search():
    def __init__(self, search, gui):

        self.window = gui.window

        try:
            self.yt = pytube.Search(search)
            self.results = self.yt.results

            self.info = []

            self.tableIndex = 0

            for x in range(10):
                self.info.append([self.results[x].title, getVideoLength(self.results[x].length), getVideoSize(self.results[x].streams.get_highest_resolution().filesize),  getVideoSize(self.results[x].streams.get_audio_only().filesize)])

            self.updateGui()
            gui.showGuiSearch()

        except pytube.exceptions.PytubeError:
            errorPopUp('Errore durante la ricerca')
            gui.clearGuiSearch()

        except:
            errorPopUp('Errore riscontrato, provare a:\n- Controllare Connessione\n- Riavviare app\n- Contattare sviluppatore')
            gui.clearGuiSearch()

    def updateGui(self):
        self.window['-SEARCH_TABLE-'].update(values=self.info)
    
    def getTableIndex(self, values):
        if self.window['-SEARCH_RESET-'].visible and not self.window['-SEARCH_DOWNLOAD-'].visible:
            self.window['-SEARCH_RESET-'].update(visible=False)
            self.window['-SEARCH_DOWNLOAD-'].update(visible=True)
            self.window['-SEARCH_RESET-'].update(visible=True)
            self.window['-SEARCH_PROGRESSBAR-'].update(visible=True)
        try: 
            self.tableIndex = self.info.index([self.info[row] for row in values][0])
        except:
            pass

    def downloadVideoAndAudio(self):
        try:
            self.results[self.tableIndex].register_on_progress_callback(self.progressFunction)
            self.results[self.tableIndex].register_on_complete_callback(self.completeFunction)
            self.results[self.tableIndex].streams.get_highest_resolution().download(getDownloadPath())
        except:
            errorPopUp('Errore durante il download')

    def downloadAudio(self):
        try:
            self.results[self.tableIndex].register_on_progress_callback(self.progressFunction)
            self.results[self.tableIndex].register_on_complete_callback(self.completeFunction)
            self.results[self.tableIndex].streams.get_audio_only().download(getDownloadPath())
        except:
            errorPopUp('Errore durante il download')

    def progressFunction(self, stream, chunk, bytes_remaining):
        current = ((stream.filesize - bytes_remaining)/stream.filesize)
        percent = current*100

        self.window['-SEARCH_PROGRESSBAR-'].update(percent)

    def completeFunction(stream, file_path, self):
        d = Download()

        while True:
            event, values = d.window.Read()

            if event == None or event == '-CLOSE-':
                break
            if event == '-OPEN_FOLDER-':
                match platform.system():
                    case 'Darwin':
                        os.system(f'open {os.path.realpath(getDownloadPath())}')
                    case 'Linux':
                        os.system(f'open {os.path.realpath(getDownloadPath())}')
                    case 'Window':
                        os.system(f'start {os.path.realpath(getDownloadPath())}')

        d.window.close()