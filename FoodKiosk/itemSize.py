from item import Item
from size import Size

class ItemSize(Item):
    def __init__(self, number, name, size, price):
        super().__init__(number, name)
        self.size = Size(size)
        self.price = price
    
    def getSize(self):
        return self.size
    
    def getPrice(self):
        return self.price
    
    def __str__(self):
        return str(super()) + ", " + str(self.size) + ", $" + self.price