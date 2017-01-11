# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

# The function should multiply each value in the list by the second argument. For example, let's say: 

# a = [2,4,10,16] 
# Then:
# b = multiply(a, 5) 
# print b
# Should print [10, 20, 50, 80 ].

def multiply(my_list, multiple):
	new_list = []
	for n in my_list:
	  new_list.append(n * multiple)
	return new_list

# works by passing the raw list as an argument
print multiply([2,4,10,16], 5)

# also works by passing a variable as an argument
a = [2,4,10,16]
b = multiply(a, 5)
print b