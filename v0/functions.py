import pytube
import pathlib
from filehandle import file as f
from cryptography.fernet import Fernet
from time import sleep
import wikipedia


class ai:
    '''
    all main ai related functions
    '''
    def __init__(self): 
        self.passfile = f("v0/pass.txt")
        self.password = self.passfile.data

    def _quit(self):
        '''
        quit the whole program
        '''
        print("quiting.........")
        sleep(5)

    def first(self):
        '''
        only for first use or to assign password
        '''
        a = input("password/open?: ")
        b = ""
        while True:
            if "pass" in a:
                if a == "password":
                    b = input("enter password: ")
                    break
                else:
                    c = input("do u mean 'password'(y/n): ")
                    if c == "y":
                        b = input("enter password: ")
                        break
                    else:
                        pass
            else:
                print("done!! your program is going to be accessible to all")
                break
        self.passfile.write(binaryencrypt(b).encrypt())
        sleep(1)

    def passCheck(self):
        '''
        check weather password is correct or not
        '''
        a = input("password: ")
        if a == binaryencrypt().adecrypt(self.passfile.data):
            return 'pass'
        else:
            self._quit()
            return 'wrong'
    
    def passchange(self):
        '''
        changes the password
        '''
        check = self.passCheck()
        if check == 'pass':
            self.first()
        else:
            print('error')
        
        

# still in work
class search:
    '''
    searchs for geo locations, songs, any find of webpage\'s description and more
    '''
    def __init__(self,query) -> None:
        self.query = query

    def brief(self):
        return wikipedia.search(self.query)



    

class binaryencrypt:
    def __init__(self,text='whoknows') -> None:
        self.text = text
        self.asscilist = []
        self.binarylist = []
        self.binarystring = ''

    def asscifind(self):
        for i in self.text:
            self.asscilist.append(ord(i))
        return self.asscilist
    
    def binaryfind(self):
        for i in self.asscilist:
            self.binarylist.append(bin(i))
        return self.binarylist
    
    def encrypt(self):
        self.asscifind()
        self.binaryfind()
        for i in self.binarylist:
            self.binarystring += i
        return self.binarystring
    
    def decrypt(self):
        dlist = []
        for i in self.binarystring.split('0b'):
            dlist.append('0b'+i)
        dlist.remove('0b')
        d=[]
        for i in dlist:
            d.append(int(i,2))
        dlist=d
        d=''
        for i in dlist:
            d+= chr(i)
        return d
    
    def adecrypt(self,dcrypt):
        dlist = []
        for i in dcrypt.split('0b'):
            dlist.append('0b'+i)
        dlist.remove('0b')
        d=[]
        for i in dlist:
            d.append(int(i,2))
        dlist=d
        d=''
        for i in dlist:
            d+= chr(i)
        return d

class paths:
    '''
    returns path of the file in with it is running or can just make a new folder
    '''
    def __init__(self) -> None:
        self.currentFilePath = self.path()

    def path():
        '''returns the file in which this is running'''
        path = str(pathlib.Path(__file__))
        path = path[::-1]
        npath = ""
        j = 0
        for i in path:
            if i == "\\" and j == 0:
                j += 1
            elif j == 1:
                npath += i
            else:
                pass
        return npath[::-1]

    def folder(self, name: str) -> str:
        """creates a new folder and gives returns its path"""
        return self.currentFilePath + "\\" + name


# stillinwork
def downloadyt(link):
    '''
    downloads video with the help of its url
    '''
    link = input("link: ")
    while True:
        try:
            vid = pytube.YouTube(link)
            break
        except:
            print("connection error")
    output = vid.video_id
    vid.set_filename("video")
    final_output = vid.get(output[-1].extension, output[-1].resolution)
    path = paths.folder("downloads")
    while True:
        try:
            final_output.download(path)
            break
        except:
            print("connection error")
    print(f"your file is in the folder {path}")



# only of test

if __name__ == "__main__":
    ai().passchange()
    pass