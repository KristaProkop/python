my_list = [6, 5, 3, 1, 8, 7, 2, 4]

#expected result: [5, 3, 1, 6, 7, 2, 4, 8]

for i in range( (len(my_list)-1) ):
    if my_list[i] > my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print my_list
