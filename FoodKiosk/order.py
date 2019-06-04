from account import Account
from customizedItem import CustomizedItem

class Order():
    def __init__(self, account, items):
        self.account = account
        self.items = items

    def getAccount(self):
        return self.account
    
    def getItems(self):
        return self.items

    def calculateCost(self):
        cost = 0.0
        for item in self.items:
            cost += item.getFullPrice()
        cost -= self.applyDiscounts()
        return cost

    def applyDiscounts(self):
        discounts = 0.0
        for item in self.items:
            for coupon in self.account.getCoupons():
                if item.getNumber() == coupon.getItem().getNumber():
                    if self.askBeforeApplyingCoupon(coupon):
                        discounts += coupon.getPriceReduction()
                        self.account.removeCoupon(coupon)
        return discounts
    

    def askBeforeApplyingCoupon(self, coupon):
        message = "Congratulations! You may redeem coupon "
        message += coupon.getName()
        message += " and save $"
        message += str(coupon.getPriceReduction())
        message += ". Would you like to redeem this offer? (y/n)"

        pleaseRedeem = input(message).strip().lower()
        while pleaseRedeem != "y" and pleaseRedeem != "n":
            pleaseRedeem = input("Invalid input; please enter y or n: ")
        if pleaseRedeem == "y":
            return True
        else:
            return False

    def processOrder(self):
        cost = self.calculateCost()
        message = "Your Order: \n"
        for item in self.items:
            message += item.getName()
            message += " Size:"
            message += item.getSize().getName()
            message += " @ original price "
            message += str(item.getPrice())
            message += "\n"
            for customization in item.getCustomizations():
                message += str(customization)
                message += "\n"
        message += "************ Order Price With Discounts ************"
        message += "$"
        message += str(cost)
        message += "\n"
        print(message)






