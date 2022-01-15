################
# Author: Andrew Wang
# Date: 9/29/2019
# This program allows the user to input total number of years and rainfall amount for each month
#   and the program will calculate total number of months, total rainfall, and monthly average rainfall.
#################

#Allows user to input number of years
years = int(input('Enter the number of years: '))

#Initialize index variables
index = 0
year_count = 1
total = 0

#If statement to determine if total number of years is positive 
if years <= 0:
    print('Invalid input.')

else:
    
    #While loop to determine if count is less than years
    while index < years:
        index = index + 1
        print('For year No.', year_count)
        Jan = float(input('Enter the rainfall amount for Jan.: '))
        Feb = float(input('Enter the rainfall amount for Feb.: '))
        Mar = float(input('Enter the rainfall amount for Mar.: '))
        Apr = float(input('Enter the rainfall amount for Apr.: '))
        May = float(input('Enter the rainfall amount for May.: '))
        Jun = float(input('Enter the rainfall amount for Jun.: '))
        Jul = float(input('Enter the rainfall amount for Jul.: '))
        Aug = float(input('Enter the rainfall amount for Aug.: '))
        Sept = float(input('Enter the rainfall amount for Sept.: '))
        Oct = float(input('Enter the rainfall amount for Oct.: '))
        Nov = float(input('Enter the rainfall amount for Nov.: '))
        Dec = float(input('Enter the rainfall amount for Dec.: '))
        
        year_count = year_count + 1
        total = (Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sept + Oct + Nov + Dec ) + total   

    #Calculates average rainfall
    average = total / (12 * years)
    
    print('There are %d months.' %(12 * years))
    print('The total rainfall is %.2f inches.' %total)
    print('The monthly average rainfall is %.2f inches.' %average)




            
            
            


        

