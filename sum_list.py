# Create a program that prints the sum of all the values in the list: 

a = [1, 2, 5, 10, 255, 3]
total = 0
for element in a:
  total = total + element
print total

#or

total = sum(a)
print total