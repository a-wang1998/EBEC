################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs allows user to enter 10-character telephon number with alphabetic characters and converts
#   and displays the orginal telephone into numeric equivalent.
##################
#Main function
def main():
    #Allows user to input telephone number
    tele_num = input(str('Enter the telephone number in the format XXX-XXX-XXXX: '))
    #Spilts the telephone number into 3 sections
    tele_num = tele_num.replace('-', ' ')
    tele_num = (tele_num.split())
    split_num = []

    #For loop that spilts each words into letters
    for i in range(1, len(tele_num)):
        split = list(tele_num[i])

        #For loop that replace letter to number
        for j in range(len(split)):
            if split[j] == 'A' or split[j] == 'B' or split[j] == 'C':
                split[j] = str(2)
            elif split[j] == 'D' or split[j] == 'E' or split[j] == 'F':
                split[j] = str(3)
            elif split[j] == 'G' or split[j] == 'H' or split[j] == 'I':
                split[j] = str(4)
            elif split[j] == 'J' or split[j] == 'K' or split[j] == 'L':
                split[j] = str(5)
            elif split[j] == 'M' or split[j] == 'N' or split[j] == 'O':
                split[j] = str(6)
            elif split[j] == 'P' or split[j] == 'Q' or split[j] == 'R' or split[j] == 'S':
                split[j] = str(7)
            elif split[j] == 'T' or split[j] == 'U' or split[j] == 'V':
                split[j] = str(8)
            elif split[j] == 'W' or split[j] == 'X' or split[j] == 'Y' or split[j] == 'Z':
                split[j] = str(9)
        split_num += split

    #Combining replaced number  
    new_num = split_num[0] + split_num[1] + split_num[2] + '-' + split_num[3] + split_num[4] + split_num[5] + split_num[6]
        
    print(tele_num[0] + '-' + new_num)
        
main()
