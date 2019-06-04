from coupon import Coupon

class Account():
    def __init__(self, number, firstName, lastName, email, coupons):
        self.number = number,
        self.firstName = firstName,
        self.lastName = lastName,
        self.email = email,
        self.coupons = coupons
    
    def getNumber(self):
        return self.number
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getEmail(self):
        return self.email
    
    def getCoupons(self):
        return self.coupons
    
    def getCouponByNumber(self, number):
        for item in self.coupons:
            if item.getCode() == number:
                return item
            # Return a null coupon if none of this account's coupons don't match the one passed in.
            return Coupon(-1, "Null Coupon", datetime.datetime(2000, 1, 1), datetime.datetime.now(), Item(-1, "Null Item"), -1)

    def addCoupon(self, coupon):
        self.coupons.append(coupon)
    
    def removeCoupon(self, coupon):
        self.coupons.remove(coupon)

    def removeExpiredCoupons(self):
        for item in self.coupons:
            if item.expirationDate < datetime.datetime.now():
                self.coupons.remove(item)
    

    


