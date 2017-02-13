# Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

class Bike(object):
  def __init__(self, price, max_speed, miles=0):
    print "new bike"
    self.price = price
    self.max_speed = max_speed
    self.miles = miles

  def displayInfo(self):
    print "Max speed is", self.max_speed
    print "Price is", self.price
    print "Total miles =", self.miles

  def ride(self):
    print "riding"
    self.miles = self.miles + 10
    return self

  def reverse(self):
    print "Reversing"
    if self.miles <= 5:
      self.miles = 0
    else:
      self.miles = self.miles - 5
    return self


bike1 = Bike(200, "25mph")
bike2 = Bike(250, "40mph")
bike3 = Bike(100, "10mph")

bike1.ride().ride().ride().reverse()
bike2.ride().reverse().ride().reverse()
bike3.reverse().reverse().reverse()

# for x in range(0, 3):
#   bike1.ride()
# bike1.reverse()
# bike1.displayInfo()

# for x in range(0, 2):
#   bike2.ride().reverse()
#   # bike2.reverse()
# bike2.displayInfo()

# for x in range(0, 3):
#   bike3.reverse()
# bike3.displayInfo()



