################
# Author: Andrew Wang
# Date: 11/10/2019
# This programs simulates a Magic 8 Ball and allows user to input question which
#   it gives a random response
#################
import random

#Main function
def main():
    #Opens and reads file
    ball = open('8_ball_responses.txt', 'r',encoding='utf8',errors="ignore")
    line = ball.readlines()

    #For loop that reads file and puts it into a list
    for i in range(len(line)):
        line[i] = line[i].rstrip('\n')

    #While function that keeps looping
    while True:
        number = random.randint(0,len(line))
        response = input(str('Enter your question: '))

        #If statement that determins if the user wants to quit or not
        if response == 'Quit':
            print('Thanks for playing.')
            break
        
        else:
            print(line[number])

#Calls main function
main()
        
