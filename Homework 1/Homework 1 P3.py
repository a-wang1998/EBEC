################
# Author: Andrew Wang
# Date: 9/7/2019
# This program calculates the number of sugar, butter, and flour needed to
#   bake the number of cookies the user has inputted
#################

#principle amount orginally deposited into account
p_amount = float(input('P= '))
#annual interest rate
interest_rate = float(input('r= '))
#number of times per year that the interest rate is compounded
num_comp = float(input('n= '))
#specified number of year
spec_year = str(input('t= '))

#amount of money in the account after specified number of years
money_amount = p_amount * (1 + (interest_rate / (num_comp * 100))) ** (num_comp * float(spec_year))

print('At the end of ' +spec_year+ ' years you will have')
print('$', format(money_amount, ',.2f'),)
