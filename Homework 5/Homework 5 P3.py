################
# Author: Andrew Wang
# Date: 10/13/2019
# This program that lets user play the game of Rock, Paper, Scissors against the computer. 
#################

import random

#Generates infinite loop
while True:
    
    #Computer generates a random number
    computer = random.randint(1,3)

    #If statement to coorespond each computer choice to rock, paper or scissors
    if computer == 1:
        computer_choice = 'rock'
    elif computer == 2:
        computer_choice = 'paper'
    elif computer == 3:
        computer_choice = 'scissors'

    #Allows user to input    
    player = int(input('Enter 1 for rock, 2 for paper, 3 for scissors: '))

    #If statement to coorespond each player choice to rock, paper or scissors
    if player == 1:
        player_choice = 'rock'
    elif player == 2:
        player_choice = 'paper'
    elif player == 3:
        player_choice = 'scissors'
    else:
        player_choice = 'something went wrong'

    #If statement to determin if the player chose the correct choice.
    if player >= 1 and player <= 3:

        #If statement to determine who wins
        if (computer == 1 and player == 1) or (computer == 2 and player == 2) or (computer == 3 and player == 3):
            print('Computer chose ' +computer_choice)
            print('You chose ' +player_choice)
            print('You made the same choice as the computer. Starting over')
        elif (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
            print('Computer chose ' +computer_choice)
            print('You chose ' +player_choice)
            print('The player wins the game.')
            break
        elif (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):
            print('Computer chose ' +computer_choice)
            print('You chose ' +player_choice)
            print('The computer wins the game.')
            break

    else:
        print('Computer chose ' +computer_choice)
        print('You chose ' +player_choice)
        print('You made an invalid choice. No winner')
        break


    
