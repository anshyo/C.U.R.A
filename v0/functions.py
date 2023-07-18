import pytube 
import pathlib
import os
from filehandle import file as f

class ai:
    def __init__(self) -> None:
        self.password = f('v0/pass').data
        

class paths:
    def __init__(self) -> None:
        self.currentFilePath = self.path()

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
        return npath[::-1]
    
    def folder(self , name : str) -> str:
        '''creates a new folder and gives returns its path'''
        return self.currentFilePath + '\\' + name
        

# stillinwork
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
    path = paths.folder('downloads')
    while True:
        try:
            final_output.download(path)
            break
        except:
            print('connection error')
    print(f'your file is in the folder {path}')





# only of test

if __name__ == '__main__':
    print(f('v0/pass.txt').data)