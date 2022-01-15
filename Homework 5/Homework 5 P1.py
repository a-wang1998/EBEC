################
# Author: Andrew Wang
# Date: 10/13/2019
# This program that gives simple math quizes and allows user to input the answer and displays if
#   the answer is correct or not.
#################

import random
#Randomly generates two number
number1 = random.randint(0,999)
number2 = random.randint(0,999)
print('%5d' %number1)
print('+%4d' %number2)

#Allows user to input answer
input_sum = int(input('Enter sum of numbers: '))

#If statement that determines if the user answers correctly or not 
if input_sum == (number1 + number2):
    print('Correct answer - Good Work!')

else:
    print('Incorrect... The correct answer is: %d' %(number1 + number2))
