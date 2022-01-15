################
# Author: Andrew Wang
# Date: 10/13/2019
# This program generates a random integer in the range from 1 to 10,
#   and asks the users to guess the number.
#################

import random

#Generates a random number between 1 to 10
random_num = random.randint(1,10)

#Generates an infinite loop
while True:
    
    #Allows the user to input a guess
    guess = int(input('Enter a number between 1 and 10, or 0 to quit: '))

    #If statement to determine if the guess is correct, too high, too low, or if user wants to quit.
    if guess > 10 or guess < 0:
        print('You guess is out of range, try again.')

    elif guess == 0:
        print('Thanks for playing!')
        break

    elif guess > random_num:
        print('Too high, try again.')

    elif guess < random_num:
        print('Too low, try again.')

    elif guess == random_num:
        print('Congratulations! You guessed the right number!')
        print('\n')
        print('A new random integer is generated.')
        random_num = random.randint(1,10)

    
 

    
    
    





































































































































