import math
import urllib
import time
import PySimpleGUI as sg
from config import *

def getVideoSize(sizeBytes):
    if sizeBytes == 0:
       return "0B"
    sizeName = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(sizeBytes, 1024)))
    p = math.pow(1024, i)
    s = round(sizeBytes / p, 2)
    return "%s %s" % (s, sizeName[i])

def getVideoLength(length):
    return time.strftime("%H:%M:%S", time.gmtime(length))

def getVideoThumbnail(url):
    fileName = 'image.png'
    filePath = './'
    fullPath = '{}{}'.format(filePath, fileName)

    urllib.request.urlretrieve(url, fullPath)

def errorPopUp(type):
        sg.popup_auto_close(f'{type}', font=fontFamily + ' ' + str(int(fontSize/2)), keep_on_top=True, auto_close_duration=7)