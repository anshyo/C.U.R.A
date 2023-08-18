class file:
    def __init__(self, path) -> None:
        self.path = path
        self.data = self.dataFetch()

    def openf(self, mode):
        return open(self.path, mode)

    def dataFetch(self):
        h = ''
        for i in self.openf('r'):
            h += i
        return h

    def cleanf(self):
        self.openf('r+').truncate(0)

    def selfwrite(self):
        self.openf('w').write(self.data.strip())
        self.openf('w').close()

    def write(self,data:str|int|float='anything') -> str|int|float:
        """writes data in the file"""
        self.openf('w').write(data)
        self.openf('w').close()

    def append(self,data:str|int|float='anything') -> str|int|float:
        """appends data in the file"""
        self.openf('a').write(data)
        self.openf('a').close()

    def comment(self, keyword):
        self.newData = ''
        for i in self.openf('r'):
            if keyword in i:
                if '#' in i:
                    pass
                else:
                    i = '# ' + i
            self.newData += i
        self.data = self.newData
        self.openf('r').close()
        self.cleanF()
        self.selfwrite()
    