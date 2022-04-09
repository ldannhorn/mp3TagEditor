import dearpygui.dearpygui as dpg
import dearpygui_ext.themes as dpgx
import main
import webbrowser
import keyboard
import time
import tkinter as tk
from tkinter import filedialog
import os
import string
import random

global debug
debug = False
file_path = ''
global currentTheme
currentTheme = dpg.theme()

datapath = os.getenv('APPDATA')

if os.path.isfile(datapath+'/mp3Suite.conf'):
    firstTime = False
else:
    firstTime = True
    open(datapath+'/mp3Suite.conf', "x")





dpg.create_context()
isRefresh = False

########################################################
def callbackMenubarOpenNoRefresh():
    callbackMenubarOpen(False)



def callbackMenubarOpen(isRefresh):
    print('callbackMenubarOpen')
    if isRefresh == False:
        root = tk.Tk()
        root.withdraw()
        global file_path
        file_path = filedialog.askopenfilename(title='mp3Suite', filetypes=[("Music File", ".mp3 .wav")])
    isRefresh = False

    dpg.set_viewport_title(title=f'mp3Suite - {file_path}')

    #Delete Existing Windows
    try:
        dpg.delete_item('file_info')
        dpg.delete_item('edit_tags')
    except: pass

    #Find Filetype
    file_ending = file_path[len(file_path)-3:].lower()
    print(file_ending)

    ## File Info
    if file_ending == 'mp3':
        with dpg.window(label='File Info', no_close=True, no_move=True, no_collapse=True, pos=(0,20), tag='file_info', width=600, height=400, no_resize=True):  #theme=currentTheme
            with dpg.tab_bar():
                with dpg.tab(label='ID3v1'):
                    dpg.add_text(f'File: {file_path}')
                    dpg.add_text(f"Artist: {main.getTag(file_path,'artist',1)}")
                    dpg.add_text(f"Album: {main.getTag(file_path,'album',1)}")
                    dpg.add_text(f"Song: {main.getTag(file_path,'song',1)}")
                    dpg.add_text(f"Track: {main.getTag(file_path,'track',1)}")
                    dpg.add_text(f"Comment: {main.getTag(file_path,'comment',1)}")
                    dpg.add_text(f"Year: {main.getTag(file_path,'year',1)}")
                    dpg.add_text(f"Genre: {main.getTag(file_path,'genre',1)}")
                    dpg.add_button(label='Refresh', callback=callbackFileInfoButtonRefresh)
                with dpg.tab(label='ID3v2'):
                    dpg.add_text(f'File: {file_path}')
                    dpg.add_text(f"Artist: {main.getTag(file_path,'artist',2)}")
                    dpg.add_text(f"Album: {main.getTag(file_path,'album',2)}")
                    dpg.add_text(f"Song: {main.getTag(file_path,'song',2)}")
                    dpg.add_text(f"Track: {main.getTag(file_path,'track',2)}")
                    dpg.add_text(f"Comment: {main.getTag(file_path,'comment',2)}")
                    dpg.add_text(f"Year: {main.getTag(file_path,'year',2)}")
                    dpg.add_text(f"Genre: {main.getTag(file_path,'genre',2)}")
                    dpg.add_text(f"Band: {main.getTag(file_path,'band',2)}")
                    dpg.add_text(f"Composer: {main.getTag(file_path,'composer',2)}")
                    dpg.add_text(f"Copyright: {main.getTag(file_path,'copyright',2)}")
                    dpg.add_text(f"URL: {main.getTag(file_path,'url',2)}")
                    dpg.add_text(f"Publisher: {main.getTag(file_path,'publisher',2)}")
                    dpg.add_button(label='Refresh', callback=callbackFileInfoButtonRefresh)
                #dpg.add_button(label='Refresh', callback=callbackFileInfoButtonRefresh)
                
    else:
        with dpg.window(label='File Info', no_close=True, no_move=True, no_collapse=True, pos=(0,20), tag='file_info', width=600, no_resize=True):  #theme=currentTheme
            dpg.add_text(f'File: {file_path}')

    ## Edit Tags
    if file_ending == 'mp3':
        with dpg.window(label='Edit Tags', no_close=True, no_move=True, no_collapse=True, pos=(600,20), tag='edit_tags', width=300, height=400, no_resize=True):
            with dpg.tab_bar():
                with dpg.tab(label='ID3v1'):
                    dpg.add_button(label='Edit Tag: Artist', callback=callbackChangeTagArtist1)
                    dpg.add_button(label='Edit Tag: Album', callback=callbackChangeTagAlbum1)
                    dpg.add_button(label='Edit Tag: Song', callback=callbackChangeTagSong1)
                    dpg.add_button(label='Edit Tag: Track', callback=callbackChangeTagTrack1)
                    dpg.add_button(label='Edit Tag: Comment', callback=callbackChangeTagComment1)
                    dpg.add_button(label='Edit Tag: Year', callback=callbackChangeTagYear1)
                    dpg.add_button(label='Edit Tag: Genre', callback=callbackChangeTagGenre1)
                with dpg.tab(label='ID3v2'):
                    dpg.add_button(label='Edit Tag: Artist', callback=callbackChangeTagArtist2)
                    dpg.add_button(label='Edit Tag: Album', callback=callbackChangeTagAlbum2)
                    dpg.add_button(label='Edit Tag: Song', callback=callbackChangeTagSong2)
                    dpg.add_button(label='Edit Tag: Track', callback=callbackChangeTagTrack2)
                    dpg.add_button(label='Edit Tag: Comment', callback=callbackChangeTagComment2)
                    dpg.add_button(label='Edit Tag: Year', callback=callbackChangeTagYear2)
                    dpg.add_button(label='Edit Tag: Genre', callback=callbackChangeTagGenre2)
                    dpg.add_button(label='Edit Tag: Band', callback=callbackChangeTagBand2)
                    dpg.add_button(label='Edit Tag: Composer', callback=callbackChangeTagComposer2)
                    dpg.add_button(label='Edit Tag: Copyright', callback=callbackChangeTagCopyright2)
                    dpg.add_button(label='Edit Tag: URL', callback=callbackChangeTagURL2)
                    dpg.add_button(label='Edit Tag: Publisher', callback=callbackChangeTagPublisher2)
                    dpg.add_button(label='Edit Tag: Image', callback=callbackChangeTagImage2)

def callbackFileInfoButtonRefresh():
    dpg.delete_item('file_info')
    dpg.delete_item('edit_tags')
    try:
        dpg.delete_item('changeTagArtist1_window')
        dpg.delete_item('changeTagAlbum1_window')
        dpg.delete_item('changeTagSong1_window')
        dpg.delete_item('changeTagTrack1_window')
        dpg.delete_item('changeTagComment1_window')
        dpg.delete_item('changeTagYear1_window')
        dpg.delete_item('changeTagGenre1_window')

        dpg.delete_item('changeTagArtist2_window')
        dpg.delete_item('changeTagAlbum2_window')
        dpg.delete_item('changeTagSong2_window')
        dpg.delete_item('changeTagTrack2_window')
        dpg.delete_item('changeTagComment2_window')
        dpg.delete_item('changeTagYear2_window')
        dpg.delete_item('changeTagGenre2_window')
        dpg.delete_item('changeTagBand2_window')
        dpg.delete_item('changeTagComposer2_window')
        dpg.delete_item('changeTagCopyright2_window')
        dpg.delete_item('changeTagURL2_window')
        dpg.delete_item('changeTagPublisher2_window')
        dpg.delete_item('changeTagImage2_window')
    except: pass

    callbackMenubarOpen(True)


## Artist 1
def callbackChangeTagArtist1():
    try: dpg.delete_item('changeTagArtist1_window')
    except: pass
    with dpg.window(label='Edit Tag: Artist - ID3v1', pos=(300,200), tag='changeTagArtist1_window', width=250, on_close=onCloseTagArtist1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'artist', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagArtist1)
            dpg.add_button(label='Save', callback=saveChangeTagArtist1)
def loggerChangeTagArtist1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagArtist1
    logChangeTagArtist1 = app_data
def saveChangeTagArtist1():
    main.newChangeTagArtist(1,file_path,str(logChangeTagArtist1))
    try: dpg.delete_item('changeTagArtist1_window')
    except: pass
def onCloseTagArtist1():
    try: dpg.delete_item('changeTagArtist1_window')
    except: pass

## Album 1
def callbackChangeTagAlbum1():
    try: dpg.delete_item('changeTagAlbum1_window')
    except: pass

    with dpg.window(label='Edit Tag: Album - ID3v1', pos=(300,200), tag='changeTagAlbum1_window', width=250, on_close=onCloseTagAlbum1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'album', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagAlbum1)
            dpg.add_button(label='Save', callback=saveChangeTagAlbum1)
def loggerChangeTagAlbum1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagAlbum1
    logChangeTagAlbum1 = app_data
def saveChangeTagAlbum1():
    main.newChangeTagAlbum(1,file_path,str(logChangeTagAlbum1))
    try: dpg.delete_item('changeTagAlbum1_window')
    except: pass
def onCloseTagAlbum1():
    try: dpg.delete_item('changeTagAlbum1_window')
    except: pass

## Song 1
def callbackChangeTagSong1():
    try: dpg.delete_item('changeTagSong1_window')
    except: pass
    with dpg.window(label='Edit Tag: Song - ID3v1', pos=(300,200), tag='changeTagSong1_window', width=250, on_close=onCloseTagSong1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'song', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagSong1)
            dpg.add_button(label='Save', callback=saveChangeTagSong1)
def loggerChangeTagSong1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagSong1
    logChangeTagSong1 = app_data
def saveChangeTagSong1():
    main.newChangeTagSong(1,file_path,str(logChangeTagSong1))
    try: dpg.delete_item('changeTagSong1_window')
    except: pass
def onCloseTagSong1():
    try: dpg.delete_item('changeTagSong1_window')
    except: pass

## Track 1
def callbackChangeTagTrack1():
    try: dpg.delete_item('changeTagTrack1_window')
    except: pass
    with dpg.window(label='Edit Tag: Track - ID3v1', pos=(300,200), tag='changeTagTrack1_window', width=280, on_close=onCloseTagTrack1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'track', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Integers)', tab_input=True, callback=loggerChangeTagTrack1, no_spaces=True, decimal=True)
            dpg.add_button(label='Save', callback=saveChangeTagTrack1)
def loggerChangeTagTrack1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagTrack1
    try: logChangeTagTrack1 = int(app_data)
    except: logChangeTagTrack1 = app_data
def saveChangeTagTrack1():
    main.newChangeTagTrack(1,file_path,str(logChangeTagTrack1))
    try: dpg.delete_item('changeTagTrack1_window')
    except: pass
def onCloseTagTrack1():
    try: dpg.delete_item('changeTagTrack1_window')
    except: pass

## Comment 1
def callbackChangeTagComment1():
    try: dpg.delete_item('changeTagComment1_window')
    except: pass
    with dpg.window(label='Edit Tag: Comment - ID3v1', pos=(300,200), tag='changeTagComment1_window', width=250, on_close=onCloseTagComment1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'comment', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagComment1)
            dpg.add_button(label='Save', callback=saveChangeTagComment1)
def loggerChangeTagComment1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagComment1
    logChangeTagComment1 = app_data
def saveChangeTagComment1():
    main.newChangeTagComment(1,file_path,str(logChangeTagComment1))
    try: dpg.delete_item('changeTagComment1_window')
    except: pass
def onCloseTagComment1():
    try: dpg.delete_item('changeTagComment1_window')
    except: pass

## Year 1
def callbackChangeTagYear1():
    try: dpg.delete_item('changeTagYear1_window')
    except: pass
    with dpg.window(label='Edit Tag: Year - ID3v1', pos=(300,200), tag='changeTagYear1_window', width=325, on_close=onCloseTagYear1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'year', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (max. 4 Characters)', tab_input=True, callback=loggerChangeTagYear1, )
            dpg.add_button(label='Save', callback=saveChangeTagYear1)
def loggerChangeTagYear1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagYear1
    logChangeTagYear1 = app_data
def saveChangeTagYear1():
    main.newChangeTagYear(1,file_path,str(logChangeTagYear1))
    try: dpg.delete_item('changeTagYear1_window')
    except: pass
def onCloseTagYear1():
    try: dpg.delete_item('changeTagYear1_window')
    except: pass

## Genre 1
def callbackChangeTagGenre1():
    try: dpg.delete_item('changeTagGenre1_window')
    except: pass
    with dpg.window(label='Edit Tag: Genre - ID3v1', pos=(300,200), tag='changeTagGenre1_window', width=420, on_close=onCloseTagGenre1):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'genre', 1))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagGenre1, no_spaces=True, decimal=True)
            dpg.add_button(label='Save', callback=saveChangeTagGenre1)
def loggerChangeTagGenre1(sender, app_data, user_data):
    print(app_data)
    global logChangeTagGenre1
    try: logChangeTagGenre1 = int(app_data)
    except: logChangeTagGenre1 = app_data
def saveChangeTagGenre1():
    main.newChangeTagGenre(1,file_path,str(logChangeTagGenre1))
    try: dpg.delete_item('changeTagGenre1_window')
    except: pass
def onCloseTagGenre1():
    try: dpg.delete_item('changeTagGenre1_window')
    except: pass



## Artist 2
def callbackChangeTagArtist2():
    try: dpg.delete_item('changeTagArtist2_window')
    except: pass
    with dpg.window(label='Edit Tag: Artist - ID3v2', pos=(300,200), tag='changeTagArtist2_window', width=250, on_close=onCloseTagArtist2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'artist', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagArtist2)
            dpg.add_button(label='Save', callback=saveChangeTagArtist2)
def loggerChangeTagArtist2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagArtist2
    logChangeTagArtist2 = app_data
def saveChangeTagArtist2():
    main.newChangeTagArtist(2,file_path,str(logChangeTagArtist2))
    try: dpg.delete_item('changeTagArtist2_window')
    except: pass
def onCloseTagArtist2():
    try: dpg.delete_item('changeTagArtist2_window')
    except: pass

## Album 2
def callbackChangeTagAlbum2():
    try: dpg.delete_item('changeTagAlbum2_window')
    except: pass
    with dpg.window(label='Edit Tag: Album - ID3v2', pos=(300,200), tag='changeTagAlbum2_window', width=250, on_close=onCloseTagAlbum2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'album', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagAlbum2)
            dpg.add_button(label='Save', callback=saveChangeTagAlbum2)
def loggerChangeTagAlbum2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagAlbum2
    logChangeTagAlbum2 = app_data
def saveChangeTagAlbum2():
    main.newChangeTagAlbum(2,file_path,str(logChangeTagAlbum2))
    try: dpg.delete_item('changeTagAlbum2_window')
    except: pass
def onCloseTagAlbum2():
    try: dpg.delete_item('changeTagAlbum2_window')
    except: pass

## Song 2
def callbackChangeTagSong2():
    try: dpg.delete_item('changeTagSong2_window')
    except: pass
    with dpg.window(label='Edit Tag: Song - ID3v2', pos=(300,200), tag='changeTagSong2_window', width=250, on_close=onCloseTagSong2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'song', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagSong2)
            dpg.add_button(label='Save', callback=saveChangeTagSong2)
def loggerChangeTagSong2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagSong2
    logChangeTagSong2 = app_data
def saveChangeTagSong2():
    main.newChangeTagSong(2,file_path,str(logChangeTagSong2))
    try: dpg.delete_item('changeTagSong2_window')
    except: pass
def onCloseTagSong2():
    try: dpg.delete_item('changeTagSong2_window')
    except: pass

## Track 2
def callbackChangeTagTrack2():
    try: dpg.delete_item('changeTagTrack2_window')
    except: pass
    with dpg.window(label='Edit Tag: Track - ID3v2', pos=(300,200), tag='changeTagTrack2_window', width=280, on_close=onCloseTagTrack2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'track', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Integers)', tab_input=True, callback=loggerChangeTagTrack2, no_spaces=True, decimal=True)
            dpg.add_button(label='Save', callback=saveChangeTagTrack2)
def loggerChangeTagTrack2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagTrack2
    try: logChangeTagTrack2 = int(app_data)
    except: logChangeTagTrack2 = app_data
def saveChangeTagTrack2():
    main.newChangeTagTrack(2,file_path,str(logChangeTagTrack2))
    try: dpg.delete_item('changeTagTrack2_window')
    except: pass
def onCloseTagTrack2():
    try: dpg.delete_item('changeTagTrack2_window')
    except: pass

## Comment 2
def callbackChangeTagComment2():
    try: dpg.delete_item('changeTagComment2_window')
    except: pass
    with dpg.window(label='Edit Tag: Comment - ID3v2', pos=(300,200), tag='changeTagComment2_window', width=250, on_close=onCloseTagComment2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'comment', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value', tab_input=True, callback=loggerChangeTagComment2)
            dpg.add_button(label='Save', callback=saveChangeTagComment2)
def loggerChangeTagComment2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagComment2
    logChangeTagComment2 = app_data
def saveChangeTagComment2():
    main.newChangeTagComment(2,file_path,str(logChangeTagComment2))
    try: dpg.delete_item('changeTagComment2_window')
    except: pass
def onCloseTagComment2():
    try: dpg.delete_item('changeTagComment2_window')
    except: pass

## Year 2
def callbackChangeTagYear2():
    try: dpg.delete_item('changeTagYear2_window')
    except: pass
    with dpg.window(label='Edit Tag: Year - ID3v2', pos=(300,200), tag='changeTagYear2_window', width=325, on_close=onCloseTagYear2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'year', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (max. 4 Characters)', tab_input=True, callback=loggerChangeTagYear2, )
            dpg.add_button(label='Save', callback=saveChangeTagYear2)
def loggerChangeTagYear2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagYear2
    logChangeTagYear2 = app_data
def saveChangeTagYear2():
    main.newChangeTagYear(2,file_path,str(logChangeTagYear2))
    try: dpg.delete_item('changeTagYear2_window')
    except: pass
def onCloseTagYear2():
    try: dpg.delete_item('changeTagYear2_window')
    except: pass

## Genre 2
def callbackChangeTagGenre2():
    try: dpg.delete_item('changeTagGenre2_window')
    except: pass
    with dpg.window(label='Edit Tag: Genre - ID3v2', pos=(300,200), tag='changeTagGenre2_window', width=420, on_close=onCloseTagGenre2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'genre', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagGenre2, no_spaces=True, decimal=True)
            dpg.add_button(label='Save', callback=saveChangeTagGenre2)
def loggerChangeTagGenre2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagGenre2
    try: logChangeTagGenre2 = int(app_data)
    except: logChangeTagGenre2 = app_data
def saveChangeTagGenre2():
    main.newChangeTagGenre(2,file_path,str(logChangeTagGenre2))
    try: dpg.delete_item('changeTagGenre2_window')
    except: pass
def onCloseTagGenre2():
    try: dpg.delete_item('changeTagGenre2_window')
    except: pass

## Band 2
def callbackChangeTagBand2():
    try: dpg.delete_item('changeTagBand2_window')
    except: pass
    with dpg.window(label='Edit Tag: Band - ID3v2', pos=(300,200), tag='changeTagBand2_window', width=420, on_close=onCloseTagBand2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'band', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagBand2)
            dpg.add_button(label='Save', callback=saveChangeTagBand2)
def loggerChangeTagBand2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagBand2
    try: logChangeTagBand2 = int(app_data)
    except: logChangeTagBand2 = app_data
def saveChangeTagBand2():
    main.newChangeTagBand(2,file_path,str(logChangeTagBand2))
    try: dpg.delete_item('changeTagBand2_window')
    except: pass
def onCloseTagBand2():
    try: dpg.delete_item('changeTagBand2_window')
    except: pass

## Composer 2
def callbackChangeTagComposer2():
    try: dpg.delete_item('changeTagComposer2_window')
    except: pass
    with dpg.window(label='Edit Tag: Composer - ID3v2', pos=(300,200), tag='changeTagComposer2_window', width=420, on_close=onCloseTagComposer2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'composer', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagComposer2)
            dpg.add_button(label='Save', callback=saveChangeTagComposer2)
def loggerChangeTagComposer2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagComposer2
    try: logChangeTagComposer2 = int(app_data)
    except: logChangeTagComposer2 = app_data
def saveChangeTagComposer2():
    main.newChangeTagComposer(2,file_path,str(logChangeTagComposer2))
    try: dpg.delete_item('changeTagComposer2_window')
    except: pass
def onCloseTagComposer2():
    try: dpg.delete_item('changeTagComposer2_window')
    except: pass

## Copyright 2
def callbackChangeTagCopyright2():
    try: dpg.delete_item('changeTagCopyright2_window')
    except: pass
    with dpg.window(label='Edit Tag: Copyright - ID3v2', pos=(300,200), tag='changeTagCopyright2_window', width=420, on_close=onCloseTagCopyright2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'copyright', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagCopyright2)
            dpg.add_button(label='Save', callback=saveChangeTagCopyright2)
def loggerChangeTagCopyright2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagCopyright2
    try: logChangeTagCopyright2 = int(app_data)
    except: logChangeTagCopyright2 = app_data
def saveChangeTagCopyright2():
    main.newChangeTagCopyright(2,file_path,str(logChangeTagCopyright2))
    try: dpg.delete_item('changeTagCopyright2_window')
    except: pass
def onCloseTagCopyright2():
    try: dpg.delete_item('changeTagCopyright2_window')
    except: pass

## URL 2
def callbackChangeTagURL2():
    try: dpg.delete_item('changeTagURL2_window')
    except: pass
    with dpg.window(label='Edit Tag: URL - ID3v2', pos=(300,200), tag='changeTagURL2_window', width=420, on_close=onCloseTagURL2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'url', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagURL2)
            dpg.add_button(label='Save', callback=saveChangeTagURL2)
def loggerChangeTagURL2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagURL2
    try: logChangeTagURL2 = int(app_data)
    except: logChangeTagURL2 = app_data
def saveChangeTagURL2():
    main.newChangeTagURL(2,file_path,str(logChangeTagURL2))
    try: dpg.delete_item('changeTagURL2_window')
    except: pass
def onCloseTagURL2():
    try: dpg.delete_item('changeTagURL2_window')
    except: pass

## Publisher 2
def callbackChangeTagPublisher2():
    try: dpg.delete_item('changeTagPublisher2_window')
    except: pass
    with dpg.window(label='Edit Tag: Publisher - ID3v2', pos=(300,200), tag='changeTagPublisher2_window', width=420, on_close=onCloseTagPublisher2):
        dpg.add_text(f'Current Value: '+main.getTag(file_path, 'publisher', 2))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint='New Value (Only Numbers from 0 to 255)', tab_input=True, callback=loggerChangeTagPublisher2)
            dpg.add_button(label='Save', callback=saveChangeTagPublisher2)
def loggerChangeTagPublisher2(sender, app_data, user_data):
    print(app_data)
    global logChangeTagPublisher2
    try: logChangeTagPublisher2 = int(app_data)
    except: logChangeTagPublisher2 = app_data
def saveChangeTagPublisher2():
    main.newChangeTagPublisher(2,file_path,str(logChangeTagPublisher2))
    try: dpg.delete_item('changeTagPublisher2_window')
    except: pass
def onCloseTagPublisher2():
    try: dpg.delete_item('changeTagPublisher2_window')
    except: pass



## Image 2
def callbackChangeTagImage2():
    try: dpg.delete_item(item='changeTagImage2_window'); dpg.delete_item(item='image')
    except: pass

    with dpg.window(label='Edit Tag: Image', pos=(300,200), tag='changeTagImage2_window', on_close=onCloseTagImage2, autosize=True):
        width, height, channels, data = dpg.load_image(main.getImage(file_path, main.get_random_string(16)+'.jpg'))
        with dpg.texture_registry():
            texture_id = dpg.add_static_texture(width, height, data)
        
        dpg.add_image(texture_id)

def onCloseTagImage2():
    try: dpg.delete_item(item='changeTagImage2_window'); dpg.delete_item(item='image')
    except: pass


















def callbackShowLicence():
    print('callbackShowLicence')
    webbrowser.open('https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode')

def callbackShowAbout():
    print('callbackShowAbout')
    with dpg.window(label='About', pos=(300,200)):   
        dpg.add_text('© Lion Dannhorn - All Rights Reserved')

def callbackExit():
    print('callbackExit')
    time.sleep(0.05)
    quit()

def messageBox(title, text):
    print('callbackMessageBox')
    with dpg.window(label=title):
        dpg.add_text(text)

def callbackSettings():
    print('callbackSettings')
    with dpg.window(label='Properties'):
        pass

def callbackLightTheme():
    print('callbackLightTheme')
    #global currentTheme
    #currentTheme =  dpgx.create_theme_imgui_light()
    dpg.bind_item_theme("main_window", dpgx.create_theme_imgui_light())
    try:
        dpg.bind_item_theme("file_info", dpgx.create_theme_imgui_light())
        dpg.bind_item_theme("edit_tags", dpgx.create_theme_imgui_light())
        # add other windows here
    except: pass
    
def callbackDarkTheme():
    print('callbackDarkTheme')
    #global currentTheme
    #currentTheme =  dpgx.create_theme_imgui_dark()
    dpg.bind_item_theme("main_window", dpgx.create_theme_imgui_dark())
    try:
        dpg.bind_item_theme("file_info", dpgx.create_theme_imgui_dark())
        dpg.bind_item_theme("edit_tags", dpgx.create_theme_imgui_dark())
        # add other windows here
    except: pass

def callbackDefaultTheme():
    print('callbackDefaultTheme')
    #global currentTheme
    #currentTheme = dpg.theme()
    dpg.bind_item_theme("main_window", theme=dpg.theme())
    try:
        dpg.bind_item_theme("file_info", theme=dpg.theme())
        dpg.bind_item_theme("edit_tags", theme=dpg.theme())
        # add other windows here
    except: pass

def callbackShowWelcome():
    with dpg.window(label='Hello!', pos=(300,200)):
        dpg.add_text("This seems to be your first time opening this application. Use the 'File' menu to open a file and edit its tags.")

########################################################




with dpg.window(tag='main_window'):
    with dpg.menu_bar():

        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Open File", shortcut="CTRL+O", callback=callbackMenubarOpenNoRefresh)
            dpg.add_menu_item(label="Exit", shortcut="CTRL+E", callback=callbackExit)
            with dpg.menu(label="Theme"):
                dpg.add_menu_item(label="Light", callback=callbackLightTheme)
                dpg.add_menu_item(label="Default", callback=callbackDefaultTheme)
                dpg.add_menu_item(label="Dark", callback=callbackDarkTheme)



        with dpg.menu(label="About"):
            dpg.add_menu_item(label="Show About", callback=callbackShowAbout)
            dpg.add_menu_item(label="Show Welcome Message", callback=callbackShowWelcome)
    
    if firstTime: callbackShowWelcome()
        

    
    


        






dpg.set_primary_window("main_window", True)

dpg.create_viewport(title='mp3TagEditor', width=1280, height=720)
#dpg.set_viewport_always_top(True)
dpg.setup_dearpygui()
#dpg.set_viewport_small_icon('XL_mp3Suite.ico')
#dpg.set_viewport_large_icon('XL_mp3Suite.ico')
dpg.show_viewport()
#dpg.start_dearpygui()


if debug: dpg.show_debug()

shortcutExit = "ctrl + E"
shortcutOpen = "ctrl + O"


while dpg.is_dearpygui_running():

    #shortcuts
    if keyboard.is_pressed(shortcutExit):
        print("shortcutExit")
        callbackExit()
    if keyboard.is_pressed(shortcutOpen):
        print("shortcutOpen")
        callbackMenubarOpen(False)
    
    #viewport title
    if file_path == '':
        dpg.set_viewport_title(title='mp3TagEditor')
    else:dpg.set_viewport_title(title=f'mp3TagEditor - {file_path}')

    #refresh
    dpg.render_dearpygui_frame()

dpg.destroy_context()
