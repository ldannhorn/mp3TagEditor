import string
import random
import os
import colorama
from colorama import Fore,Back
colorama.init()
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import eyed3
from eyed3.id3.frames import ImageFrame

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def error(text):
    print(Back.RED+Fore.WHITE + '[ERROR] ' + str(text) + Back.RESET+Fore.RESET)




def encode(lameVersion, in_file, out_file, bitrate, quality, VBR):
    nope = False
    if int(lameVersion) == 32:                          #
        command = 'lame32.exe -V2 '                     #
    if int(lameVersion) == 64:                          # Choose LAME version
        command = 'lame64.exe -V2 '                     #
    else:
        error('Invalid input at: encode:lameVersion')
        nope = True

    command = command + (str(in_file) + ' ' + str(out_file) + ' -b ' + str(int(bitrate)) + ' ') # Append filenames and bitrate

    if quality == 'high':                       #
        command = command + '-h '               #
    elif quality == 'normal':                   # Choose quality level (or don't)
        pass                                    #
    elif quality == 'fast':                     #
        command = command + '-f '               #
    else:
        error('Invalid input at: encode:quality')
        nope = True

    VBR = float(VBR)
    if VBR > 9:
        VBR = 9
    elif VBR < 0:
        VBR = 0
    command = command + '-V ' + str(VBR) + ' '

    print(command)
    if nope:
        error("Couldn't run command...")
    else:
        os.system(command)

def destroy(lameVersion, in_file, out_file, iterations):
    nope = False
    if int(lameVersion) == 32:                          #
        command = 'lame32.exe -V2 '                     #
    if int(lameVersion) == 64:                          # Choose LAME version
        command = 'lame64.exe -V2 '                     #
    else:
        error('Invalid input at: destroy:lameVersion')
        nope = True

    command += in_file + ' ' + out_file + ' -b 0 ' + '-f ' + '-V 9.999'

    os.system(command)

    for i in range(iterations):
        if int(lameVersion) == 32:                          #
            command = 'lame32.exe -V2 '                     #
        if int(lameVersion) == 64:                          # Choose LAME version
            command = 'lame64.exe -V2 '                     #
        else:
            error('Invalid input at: destroy:lameVersion')
            nope = True

        temp = get_random_string(32)
        command += out_file + ' ' + temp + '.mp3' + ' -b 0 ' + '-f ' + '-V 9.999'

        print(command)
        if nope:
            error("Couldn't run command...")
        else:
            os.system(command)
    
    print(Fore.GREEN + 'FINAL FILE: ' + temp)

# lame.exe (--tt "title") (--ta "artist") (--tl "album") (--ty "year") (--tc "comment") (--tn "track") (--tnt "total") (--tg "genre") (--ti "imagefile") 
def changeTag(lameVersion, in_file, out_file, tag, tagData):
    nope = False
    if int(lameVersion) == 32:                                  #
        command = 'lame32.exe '                                 #
    if int(lameVersion) == 64:                                  # Choose LAME version
        command = 'lame64.exe '                                 #
    else:
        error('Invalid input at: changeTag:lameVersion')
        nope = True

    command += f'{in_file} {out_file} '

    tag = str(tag)
    tag = tag.lower()
    tagData = str(tagData)
    if tag == 'title':
        command += f'--tt "{tagData}"'
    elif tag == 'artist':
        command += f'--ta "{tagData}"'
    elif tag == 'album':
        command += f'--tl "{tagData}"'
    elif tag == 'year':
        command += f'--ty "{tagData}"'
    elif tag == 'comment':
        command += f'--tc "{tagData}"'
    elif tag == 'track':
        command += f'--tn "{tagData}"'
    elif tag == 'genre':
        command += f'--tg "{tagData}"'
    elif tag == 'image':
        command += f'--ti "{tagData}"'
    else:
        error('Invalid input at: changeTag:tagData')
        nope = True
    
    print(command)
    if nope:
        error("Couldn't run command...")
    else:
        os.system(command)



def newChangeTagArtist(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.artist = input
    mp3.save()

def newChangeTagAlbum(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.album = input
    mp3.save()

def newChangeTagSong(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.song = input
    mp3.save()

def newChangeTagTrack(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.track = input
    mp3.save()

def newChangeTagComment(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.comment = input
    mp3.save() 

def newChangeTagYear(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.year = input
    mp3.save()

def newChangeTagGenre(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        mp3.set_version(VERSION_1)
    elif version == '2':
        mp3.set_version(VERSION_2)
    
    mp3.genre = input
    mp3.save()
    
def newChangeTagBand(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        error('Only Version 2! Setting Version to 2 automatically.')

    mp3.set_version(VERSION_2)
    
    mp3.band = input
    mp3.save()

def newChangeTagComposer(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        error('Only Version 2! Setting Version to 2 automatically.')

    mp3.set_version(VERSION_2)
    
    mp3.composer = input
    mp3.save()

def newChangeTagCopyright(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        error('Only Version 2! Setting Version to 2 automatically.')

    mp3.set_version(VERSION_2)
    
    mp3.copyright = input
    mp3.save()

def newChangeTagURL(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        error('Only Version 2! Setting Version to 2 automatically.')

    mp3.set_version(VERSION_2)
    
    mp3.url = input
    mp3.save()

def newChangeTagPublisher(version, file, input):
    mp3 = MP3File(file)
    input = str(input)
    
    if version == '1':
        error('Only Version 2! Setting Version to 2 automatically.')

    mp3.set_version(VERSION_2)
    
    mp3.publisher = input
    mp3.save()

def newChangeImage(file, input):
    audiofile = eyed3.load(file)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(input,'rb').read(), 'image/jpeg')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)




def getTag(file, tag, version):
    mp3 = MP3File(file)
    if version == 1:
        mp3.set_version(VERSION_1)
    elif version == 2:
        mp3.set_version(VERSION_2)
    else: error('Invalid Version at getTag:Version')
    tag = tag.lower()

    if tag == 'artist':
        return str(mp3.artist)
    if tag == 'album':
        return str(mp3.album)
    if tag == 'song':
        return str(mp3.song)
    if tag == 'track':
        return str(mp3.track)
    if tag == 'comment':
        return str(mp3.comment)
    if tag == 'year':
        return str(mp3.year)
    if tag == 'genre':
        return str(mp3.genre)
    if tag == 'band':
        return str(mp3.band)
    if tag == 'composer':
        return str(mp3.composer)
    if tag == 'copyright':
        return str(mp3.copyright)
    if tag == 'url':
        return str(mp3.url)
    if tag == 'publisher':
        return str(mp3.publisher)
    else: error('Invalid Tag at getTag:Tag')
    

def getImage(in_file, out_file):
    in_file = str(in_file)
    out_file = str(out_file)
    command = f'ffmpeg.exe -i {in_file} {out_file}'
    os.system(command)
    return out_file


#newChangeImage('F:/Programmieren/python/MP3/test.mp3', 'F:/Programmieren/python/MP3/fatmario.PNG')
#getImage('test.mp3', 'lol.jpg')