################
# Author: Andrew Wang
# Date: 10/3/2019
# This program finds prime numbers between 1 to 100
#################

#Main function
def main():
    #Initialize variables
    index = 0
    prime = 1

    #While loop that calculates prime number from 1 to 100
    while index < 100:
        prime_stat = is_prime(prime)

        #If statement that shows if inputted number is a prime or not
        if prime_stat == 'True':
            print('%d is a prime number.' %prime)
                
        elif prime_stat == 'False':
            #print('%d is not a prime number.' %prime)
            pass
            
        prime += 1
        index += 1
    
#User defined function that determines if a number is prime or not
def is_prime(prime):

    #If statement that determins a number is 1 or 2, else find if prime or not
    if prime == 1 or prime == 2:
        prime_stat = 'True'
        
        return prime_stat

    elif prime != 1 or prime != 2:
        
        #For loop that checks number from 2 to itself - 1
        for check_prime in range(2, prime, 1):

            #If statement that determines a number is prime or not
            if prime % check_prime == 0:
                prime_stat = 'False'
                return prime_stat
        
            else:
                prime_stat = 'True'

    return prime_stat

main() 

