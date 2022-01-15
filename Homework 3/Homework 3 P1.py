################
# Author: Andrew Wang
# Date: 9/29/2019
# This program allows the user to input a positive number until a negative number is inputted
#   and the program calculates the sum and average of the number inputted
#################

#Allows the user to input a number
number = float(input('Enter a positive number (negative to quit): '))

#Initiallizing total and index
index = 0
total = 0

#While loop that keeps running when the number is positive
while number >= 0:
    total = total + number
    index = index + 1
    number = float(input('Enter a positive number (negative to quit): '))

#Calculation of average 
average = total / index

print('Sum = $.2f' %total)
print('Average = %.2f' %average)

