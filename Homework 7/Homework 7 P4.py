################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs allows user to input a sentence and converts each word to Pig Latin.
#################
#Main function()
def main():
    #Allows user to input sentence
    string = input(str('Enter a string: '))

    #For loop that removes first letter of the word to the back and adding 'ay'
    for i in string.split():
        first_letter = i[0]
        rest_letter = i[1:]
        new_string = rest_letter+first_letter+'ay'
        print(new_string.upper() + ' ',end='')

#Calls main function
main()
