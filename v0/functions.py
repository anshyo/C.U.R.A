import pytube 
import pathlib
import os

def path():
    path = str(pathlib.Path(__file__))
    path = path[::-1]
    npath = ''
    j = 0
    for i in path:
        if i == '\\' and j == 0:
            j += 1
        elif j == 1:
            npath += i
        else:
            pass
    return npath[::-1]+'\\downloadedVideos'

def downloadyt(link):
    link = input('link: ')
    while True:
        try:
            vid = pytube.YouTube(link)
            break
        except:
            print('connection error')
    output = vid.video_id
    vid.set_filename('video')
    final_output = vid.get(output[-1].extension,output[-1].resolution)
    while True:
        try:
            final_output.download(path())
            break
        except:
            print('connection error')
    print(f'your file is in the folder {path()}')
    