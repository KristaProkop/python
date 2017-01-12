# Starting the program...

# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

# Ending the program, thank you!

#generate random number and round to 1 or 0
#0 represents tails, 1 represents heads
import random

print "Starting the program..."
result_list = []
for count in range(1, 5001):
    x = random.random()
    result = round(x, 0)
    result_list.append(result)
    if(result == 0):
        coin = "tails"
    else: 
        coin = "heads"
    print "Attempt # " + str(count) + ": Throwing a coin... It's a " + coin + "!... Got " + str(result_list.count(0)) + " tails and " + str(result_list.count(1)) + " heads so far"
print "Ending the program, thank you!"