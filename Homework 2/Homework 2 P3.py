################
# Author: Andrew Wang
# Date: 9/19/2019
# This program allows the user to input a pocket number between 0 and 36 and
#    and the program will determine the color of the pocket number
#################

#users inputs pocket number
pocket_num = float(input('Input a pocket number between 0 and 36: '))

#if statement that determines if pocket number is < 0 or > 36
if pocket_num < 0 or pocket_num > 36:
    print('Invalid Input!')


else:
    #if statement that determines the color of the pocket number
    if pocket_num == 0:
        print('The pocket %.0f is green' %pocket_num)

    elif pocket_num >= 1 and pocket_num <= 10:
        if (pocket_num % 2 == 0):
            print('The pocket %.0f is black' %pocket_num)

        else:
            print('The pocket %.0f is red' %pocket_num)

    elif pocket_num >= 11 and pocket_num <= 18:
        if (pocket_num % 2 == 0):
            print('The pocket %.0f is red' %pocket_num)

        else:
            print('The pocket %.0f is black' %pocket_num)

    elif pocket_num >= 19 and pocket_num <= 28:
        if (pocket_num % 2 == 0):
            print('The pocket %.0f is black' %pocket_num)

        else:
            print('The pocket %.0f is red' %pocket_num)

    elif pocket_num >= 29 and pocket_num <= 36:
        if (pocket_num % 2 == 0):
            print('The pocket %.0f is red' %pocket_num)

        else:
            print('The pocket %.0f is black' %pocket_num)

        
