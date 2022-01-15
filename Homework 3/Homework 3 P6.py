################
# Author: Andrew Wang
# Date: 9/29/2019
# This program allows the user to input number of lines and the program prints out
# "##" with space in between them as each line progresses
#################

#Allows the user to input number of lines
lines = int(input('Enter the number of lines: '))
print ("##")

#For loop that increase a space between as each line progresses
for index in range(lines - 1):
    print ("#",index * " " + "#")
        
