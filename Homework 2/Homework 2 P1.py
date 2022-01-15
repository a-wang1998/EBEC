################
# Author: Andrew Wang
# Date: 9/19/2019
# This program allows the user to input year and the program calculates if there are
#   29 days or 28 days in February
#################

#users inputs year
year = float(input('Please input a year: ')) 

#if statement that determines leap year
if (year % 100 == 0) & (year % 400 == 0):
    print("There are 29 days in Feburary in %.0f" %year)

elif (year % 100 != 0) & (year % 4 == 0):
    print("There are 29 days in Feburary in %.0f" %year)

else:
    print("There are 28 days in Feburary in %.0f" %year)

