################
# Author: Andrew Wang
# Date: 9/7/2019
# This program calculates the number of vines that will fit in a row using
#   length of the row, amount of space used by end-post assembly, and space
#    between vines
#################

#legnth of row (ft)
length = float(input('R= '))
#amount of space used by end-post assembly (ft)
amount = float(input('E= '))
#space between vines (ft)
space = float(input('S= ')) 

#calculates number of vines that will fit in the row
numofvine = ((length - 2 * amount) / space) // 1

print("You have enough space for %.0f vine(s)." %numofvine)
