import pytube
import pathlib
from filehandle import file as f
from cryptography.fernet import Fernet
from time import sleep


class ai:
    def __init__(self): 
        self.passfile = f("v0/pass.txt")
        self.password = self.passfile.data

    def _quit(self):
        print("quiting.........")
        sleep(5)

    def first(self):
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
        self.passfile.write(str(encrypT(b).binaryStrEncrypt()))
        sleep(1)

    def passCheck(self):
        a = input("password: ")
        if a == encrypT.binStrDecrypt(self.passfile.data):
            pass
        else:
            self._quit()


class paths:
    def __init__(self) -> None:
        self.currentFilePath = self.path()

    def path():
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


class encrypT:
    def __init__(self, text: str) -> None:
        self.key = Fernet(Fernet.generate_key())
        self.obj = text

    def binaryStrEncrypt(self):
        b = []
        for i in self.obj:
            b.append(self.chrBin(i))
        return b

    def binStrDecrypt(self):
        o = ""
        for i in self.:
            o += self.binChr(i)
        return o

    def chrBin(data):
        return bin(ord(data))

    def binChr(data):
        return chr(int(data, 2))

    def doEncrypt(self):
        return self.key.encrypt(self.obj.encode())

    def doSelfDecrypt(self):
        return self.key.decrypt(self.doEncrypt().decode())

    def doDecrypt(self, dat):
        return self.key.decrypt(dat.decode())


# only of test

if __name__ == "__main__":
    ai().first()
    # open('v0/pass.txt' , 'w').write('e')
