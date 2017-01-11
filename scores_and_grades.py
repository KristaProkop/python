# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this...

# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!

print "This program uses a while loop and spits out grades as the user enters each score:"

def grader(score):
  if int(score) >= 90:
    grade = "A"
  elif int(score) >= 80:
    grade = "B"
  elif int(score) >= 70:
    grade = "C"
  elif int(score) >= 60:
    grade = "D"
  else:
    grade = "F"
  print "Score =", str(score)+ "; Your grade =", grade

counter = 0
while counter <= 10:
  n = input('Enter a test score: ')
  grader(n)
  counter = counter + 1

print "\n This next program uses for loops. After asking for all of the grades it calls a method within another method to summarize the scores and grades at the end."

def summarize(scores):
  print "\n Scores and Grades"
  for element in scores:
    grader(element)
  print "End of the program. Bye!"

scores = []
for count in range(0, 5):
  n = input('Enter a test score: ')
  scores.append(n)
summarize(scores)