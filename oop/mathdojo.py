#subtract function not working

class MathDojo(object):
  def __init__(self):
    print "Calculating..."
    self.result = 0

  def add(self, num1, *num2):
    if type(num1) == list or type(num1) == tuple:
      for num in num1:
        self.result += num
    else:
      self.result += num1
    if num2:
      if type(num2) == list or type(num2) == tuple:
        for num in num2:
          self.result += num
      else:
        self.result += num2
    return self
    
  def subtract(self, num1, *num2):
    if type(num1) == list or type(num1) == tuple:
      subtotal = 0
      for num in num1:
        subtotal += num
        print subtotal
      self.result -= subtotal
    else:
      self.result = num1
    if num2:
      if type(num2) == list or type(num2) == tuple:
        subtotal = 0
        for num in num2:
          print num
          subtotal += num 
        self.result -= subtotal
      else:
        self.result -= num2
    return self


#print MathDojo().add(2).add(2, 5).subtract(3, 2).result
#print MathDojo().add([1],3,4).result
#print MathDojo().add(1, 2).subtract(2, [2, 2]).result
print MathDojo().subtract(2, [2,3], (1.1+2.3)).result
#-2-(2+3)-(1.1+2.3)

#print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
#print MathDojo().add([1],3,4).result
print MathDojo().subtract(2, [2, 3]).result
#print MathDojo().add([1],3,4).subtract(2, [2,3]).result

#print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result