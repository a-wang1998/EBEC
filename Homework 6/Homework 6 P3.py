def main():
    int_num = int(input('Enter an interger greater than 1: '))

    if int_num > 1:
        check_prime(int_num)

    else:
        print('Invalid input.')

def check_prime(int_num):
    prime_list = [0] * (int_num -1)
    prime = []
    integer = 2
    
    
    for i in range(len(prime_list)):       
        prime_list[i] = integer
        integer += 1

    #For loop that checks number from 2 to itself - 1   
    for i in range(2,len(prime_list),1):
    #If statement that determines a number is prime or not
        for j in range (2,i):
            if prime_list[i] == 2:
                print('is prime.')
            else:
                if prime_list[i] % j == 0:
                    prime.append(0)
                    break
                else:
                    print(prime_list[i])
                    prime.append(1)
                    break
    for i in range(len(prime_list)):
        if prime[i] == 0:
            print(+prime_list[i]+ 'is composite')
        else:
            print(+prime_list[i]+ 'is prime')

main()
