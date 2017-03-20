class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Max speed: " + str(self.max_speed)
        print "Miles: " + str(self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self



bike1 = Bike(200, 25)
bike1.ride().ride().ride().reverse().displayInfo()
bike2 = Bike(300, 35)
bike2.ride().ride().reverse().reverse().displayInfo()
bike3 = Bike(500, 95)
bike3.reverse().reverse().reverse().displayInfo()
