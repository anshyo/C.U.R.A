class file:
    def __init__(self, path) -> None:
        self.path = path
        self.data = ''

    def openf(self, mode):
        return open(self.path, mode)

    def dataFetch(self):
        for i in self.openf('r'):
            self.data += i

    def cleanF(self):
        self.openf('r+').truncate(0)

    def write(self, data):
        self.openf('a').write(self.data.strip())
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
        self.write(self.data.strip())
    