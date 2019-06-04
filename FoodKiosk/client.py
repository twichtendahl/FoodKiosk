import datetime
from item import Item
from size import Size
from itemSize import ItemSize
from customization import Customization
from customizedItem import CustomizedItem
from coupon import Coupon
from account import Account
from order import Order

specialSauce = Customization("Special Sauce", .25)
cream = Customization("Cream", .25)
sugar = Customization("Sugar", .00)

burgerCustomization = [specialSauce]
coffeeCustomization = [cream, cream, sugar]

cheeseburgerWithSauce = CustomizedItem(number=1, name="Cheeseburger", size="(one size only)", price=5.00, customizations=burgerCustomization)
mediumFrenchFries = CustomizedItem(2, "French Fries", "medium", 2.75, [])
smallVanillaShake = CustomizedItem(3, "Vanilla Milkshake", "small", 3.25, [])
coffeeWithTwoCreamOneSugar = CustomizedItem(4, "Coffee", "medium", 2.50, coffeeCustomization)

vanillaShakeCoupon = Coupon(100, "Memorial Day Milkshake", datetime.datetime(2019, 5, 25), datetime.datetime(2019, 6, 1), Item(3, "Vanilla Milkshake"), 1.00)

travis = Account(200, "Travis", "Wichtendahl", "travis@example.com", [vanillaShakeCoupon])

myOrder = Order(travis, [cheeseburgerWithSauce, mediumFrenchFries, smallVanillaShake, coffeeWithTwoCreamOneSugar])
myOrder.processOrder()