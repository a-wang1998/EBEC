################
# Author: Andrew Wang
# Date: 10/20/2019
# This programs compares numbers inside a list and determines if it is greater than number n
#   and creates a new list with numbers greater than n
#################
#Main function
def main():
    number_list = [19,2940,10,24,29,1,85,201,-15,-122,799]
    num_n = 13
    comparelist(number_list, num_n)

#Function that compares the numbers inside the list with number n
def comparelist(number_list, num_n):
    #Creating an empty list
    larger_list = []

    #For loop that compares the number
    for i in range(len(number_list)):
        if number_list[i] > num_n:
            larger_list.append(number_list[i])
        else:
            pass
            
    
    print('Number:', num_n)
    print('List of numbers:')
    print(number_list)
    print('List of numbers that are larger than 13:')
    print(larger_list)

main()
