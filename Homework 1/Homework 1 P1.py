################
# Author: Andrew Wang
# Date: 9/7/2019
# This program calculates the number of sugar, butter, and flour needed to
#   bake the number of cookies the user has inputed
#################

#sugar needed for 48 cookies
sugar = 1.5
#butter needed for 48 cookies
butter = 1
#flour needed for 48 cookies
flour = 2.75

#user input amount of cookies needed
cookies = float(input('How many cookies: '))

#calculates the number of sugar needed for the amount of cookies user has inputed
numofsugar = (1.5 / 48) * cookies
#calculates the number of butter needed for the amount of cookies user has inputed
numofbutter = (1 / 48) * cookies
#calculates the number of flour needed for the amount of cookies user has inputed
numofflour = (2.75 / 48) * cookies


print("%.2f cups of sugar" %numofsugar)
print("%.2f cups of butter" %numofbutter)
print("%.2f cups of flour" %numofflour)
