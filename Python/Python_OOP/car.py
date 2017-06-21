class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()
        # self.display_all()
    def tax(self):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price: " + str(self.price) + " speed: " + str(self.speed) + " fuel: " + str(self.fuel) + " mileage: " + str(self.mileage) + " Tax: " + str(self.tax)
    def __repr__(self):
        return "<Car object, price {}, speed {}, mileage {}>".format(self.price, self.speed, self.mileage)

if __name__ == '__main__':
    car1 = Car(1000, "25mph", "Half-full", "14mpg")
    car2 = Car(2000, "35mph", "Half-full", "14mpg")
    car3 = Car(3000, "45mph", "Half-full", "14mpg")
    car4 = Car(4000, "55mph", "Half-full", "14mpg")
    car5 = Car(5000, "65mph", "Half-full", "14mpg")
    car6 = Car(16000, "75mph", "Half-full", "14mpg")
