################
# Author: Andrew Wang
# Date: 9/29/2019
# This program prints out 7 * initially and decrease number of * each line until there is 1 * left
#################

#Initialize index
index = 7

#While loop to determine if index is larger than 0
while index > 0:

    #Intialize count
    count = 0

    #While loop to print out * corresponding with number of index
    while index > count:
        print('*', end='')
        count = count + 1
    print(' ')
    index = index - 1
