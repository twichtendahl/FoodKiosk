from itemSize import ItemSize
from customization import Customization

class CustomizedItem(ItemSize):
    def __init__(self, number, name, size, price, customizations):
        super().__init__(number, name, size, price)
        self.customizations = customizations
    
    def getCustomizations(self):
        return self.customizations
    
    def __str__(self):
        this = str(super()) + " with "
        for item in self.customizations:
            this = this + item + ", "
        this = this[0:len(this) - 1]
        return this

    def getFullPrice(self):
        fullPrice = self.getPrice()
        for item in self.customizations:
            fullPrice += item.getPrice()
        return fullPrice