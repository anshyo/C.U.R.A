class file:
    def __init__(self , path) -> None:
        self.path = path
        self.data = ''
    def openf(self , mode):
        return open(self.path , mode)
    def dataFetch(self):
        for i in self.openf('r'):
            self.data += i
    def commenter(self, keyword):
        