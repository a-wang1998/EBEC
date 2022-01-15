################
# Author: Andrew Wang
# Date: 9/29/2019
# This program allows the user to input number of organisms, average daily increase, days to multiply
#   and the program calculates the population of the organism each day.
#################

#Allows user to input number of organisms
num_org = float(input('Starting number of organisms: '))
#Allows user to input average daily increase
avg_inc = float(input('Average daily increae, in percent: '))
#Allows user to input number of days to multiply
days_mult = float(input('Number of days to multiply: '))

#Initializing index
index = 0
days = 0

print('Day Approximate\tPopulation')

#While loop to determine index exceedes days to multiply
while index < days_mult:
    days = days + 1
    index = index + 1
    
    print('%d\t\t\t%.4f' %(days, num_org))

    #Calculates the number of organisms each day
    num_org = num_org * (avg_inc / 100 + 1) 
    



    

