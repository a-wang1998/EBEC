################
# Author: Andrew Wang
# Date: 11/03/2019
# This programs creates a dictionary that contains U.S state as key and capital as values and the program randomly
#   quizes the player the state's capital and keep count the number of times the user is correct and incorrect
#################
import random
#Main function
def main():
    #Open and reads file
    us_s = open('us_state.txt', 'r')
    us_c = open('us_cap.txt', 'r')
    line_s = us_s.readlines()
    line_c = us_c.readlines()
    #Initializing variables
    us_sc = {}
    correct = 0
    incorrect = 0

    #Creating a list for state and capital and combining into dictionary
    for i in range(len(line_s)):
        line_s[i] = line_s[i].rstrip('\n')
        line_c[i] = line_c[i].rstrip('\n')
        us_sc[line_s[i]] = line_c[i]

    #While loop that keeps quizing the user 
    while True:
        index = random.randint(0, len(line_s) - 1)
        #Allows user to input the answer to the question
        question = str(input('What is the capital of ' +line_s[index]+ '? (or enter 0 to quit): '))

        #If statement that breaks when user enter 0
        if question == '0':
            break
        else:
            #Retrives the correct answer
            capital = us_sc.get(line_s[index])

            #If statement that determines if the user is correct and keeps count
            if question == capital:
                print('You are correct.')
                correct += 1
            else:
                print('You are incorrect.')
                incorrect += 1

    print('You had %d correct responses and %d incorrect responses.' %(correct, incorrect))

    us_state.close()
    us_cap.close()
#Calling main function
main()
    
    
