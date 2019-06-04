class Item(object):
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getNumber(self):
        return self.number

    def getName(self):
        return self.name
    
    def __str__(self):
        return str(self.number) + ": " + self.name
