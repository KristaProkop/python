
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
  
car1 = Car(20000, "180mph", "empty", "15mpg")
car2 = Car(3000, "120mph", "full", "24mpg")
car3 = Car(15000, "100mph", "full", "20mpg")
car4 = Car(10000, "120mph", "middle", "22mpg")
car5 = Car(18000, "150mph", "full", "30mpg")
car6 = Car(2000, "15mph", "kind of full", "95mpg")