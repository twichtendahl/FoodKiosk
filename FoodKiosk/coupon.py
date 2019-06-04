from item import Item
import datetime

class Coupon():
    def __init__(self, code, name, activateDate, expirationDate, item, priceReduction):
        self.code = code
        self.name = name
        self.activateDate = activateDate
        self.expirationDate = expirationDate
        self.item = item
        self.priceReduction = priceReduction

    def getCode(self):
        return self.code
    
    def getName(self):
        return self.name

    def getActivateDate(self):
        return self.activateDate
    
    def getExpirationDate(self):
        return self.expirationDate
    
    def getItem(self):
        return self.item
    
    def getPriceReduction(self):
        return self.priceReduction