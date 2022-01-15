################
# Author: Andrew Wang
# Date: 9/19/2019
# This program allows the user to input the quantity of boxes and the program will determine
#   how much discount is applied and the total price.
#################

#user inputs amount of quantity
quantity = float(input('Please input the quantity of amount package bought: '))
#price of the package
price = 99

#if statement to determine if the quantity is <0 
if quantity <= 0:
    print('Invalid Input!')

else:
    #if statement to determine the amount of quantity and apply the necessary discount
    if quantity >= 10 and quantity <= 19:
            print('10% discount applied')
            discount = 0.9
                     
    elif quantity >= 20 and quantity <= 49:
            print('25% discount applied')
            discount = 0.75
        
    elif quantity >= 50 and quantity <= 99:
            print('35% discount applied')
            discount = 0.65
        
    elif quantity >= 100:
            print('45% discount applied')
            discount = 0.55
            
    else:
            print('No discount applied')
            discount = 1

    #calculates final price with discount applied        
    total_amt = price * quantity * discount
    #prints amount of package and final price
    print('The final price for purchasing '+str(int(quantity))+ ' packages is ${:,.2f}' .format(total_amt))
