################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs that writes a series of random numbers from 1 through 500 to a file and the user will
#   input how many number will be inputed into file
#################
import random
#Main function
def main():
    #Allows the user to input the total number will be inputed into file
    number = int(input('Enter the number of random numbers to be written to the file: '))
    #Writes the file
    number_file = open('number_file.txt', 'w')

    #For loop that inputs random number into file
    for i in range(number):
        random_number = random.randint(1, 500)
        number_file.write(str(random_number) + '\n')
    number_file.close()

#Calls main function
main()
    
    
