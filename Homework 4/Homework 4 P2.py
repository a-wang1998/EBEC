################
# Author: Andrew Wang
# Date: 10/3/2019
# This program uses user define function determines input of two integers and determining which 
#   one is larger of the two.
#################

#Main function
def main():
    #Execute user defined function 
    max_udf()

#User defined function for determining two intergers and which one is larger
def max_udf():
    
    #Allows user input for first and second intergers
    first_int = float(input('Enter the fist interger: '))
    second_int = float(input('Enter the second interger: '))

    #If statement that determines if two values are intergers and which one is larger
    if (first_int % 1) == 0 and (second_int % 1) == 0:
        if first_int > second_int:
            print('%d is greater.' %first_int)
        elif second_int > first_int:
            print('%d is greater.' %second_int)
    else:
        if (first_int % 1) != 0:
            print('%.1f is not an interger.' %first_int)
        elif (second_int % 1) != 0:
            print('%.1f is not an interger.' %second_int)


main()

