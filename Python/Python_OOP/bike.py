class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Max speed: " + str(self.max_speed)
        print "Miles: " + str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        self.miles -= 5
    def __repr__(self):
        return "<Bike object, price {}, max_speed {}, miles {}>".format(self.price, self.max_speed, self.miles)

if __name__ == '__main__':
    bike1 = Bike(200, 25)
    bike1.ride()
    bike1.ride()
    bike1.ride()
    bike1.reverse()
    bike1.displayInfo()
    bike2 = Bike(300, 35)
    bike2.ride()
    bike2.ride()
    bike2.reverse()
    bike2.reverse()
    bike2.displayInfo()
    bike3 = Bike(500, 95)
    bike3.reverse()
    bike3.reverse()
    bike3.reverse()
    bike3.displayInfo()
