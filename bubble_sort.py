# my_list = [6, 5, 3, 1, 8, 7, 2, 4]


import random 
from datetime import datetime

startTime = datetime.now()


def bubble_sort(my_list):
    print "original list:\n", my_list, "\n"
    for i in range( (len(my_list)-1) ):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return my_list

random_list = [int(10000*random.random()) for i in xrange(100)]
print(bubble_sort(random_list))

print "\n Process execution time: ", (datetime.now() - startTime)


#here's another way of doing it:
#expected result: [5, 3, 1, 6, 7, 2, 4, 8]

def bubble_sort2(try_list):
    for i, j in enumerate(try_list):
        if try_list[i] < try_list[i-1]:
            try_list.remove(j)
            try_list.insert(i-1, j)
    return try_list

try_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort2(try_list))