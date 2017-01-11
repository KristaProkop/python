# Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use array to do this exercise.

for n in range(1, 1000):
  if n % 2 != 0:
    print n
    

#Create another program that prints all the multiples of 5 from 5 to 1,000,000. 

for n in range(5, 1000001):
  if n % 5 == 0:
    print n