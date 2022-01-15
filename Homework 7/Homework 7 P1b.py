################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs reads the random numbers from the file user created and displays the total of the
#    numbers in the file and also the number of random numbers read from the file.
#################
#Main function
def main():
    #Reads the user-created file
    number_file = open('number_file.txt', 'r')
    #Reads the line of user-created file
    line = number_file.readline()
    #Initializing index
    count = 0
    total_num = 0

    #While loop that reads the line of the file and calculates total number and number ead from file.
    while line != '':
        num_file = float(line)
        total_num += num_file

        line = number_file.readline()
        count += 1

    print('Total:', format(total_num,',.0f'))
    print('%.0f numbers were read from the file.' %count)
    number_file.close()

#Calls main function
main()
    
       
    
    
    
