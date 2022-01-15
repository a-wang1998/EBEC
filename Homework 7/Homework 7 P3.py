################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs reads the file and calculates the average number of words per centence
#################
#Main function
def main():
    #Opens and reads the file
    num_words = open('average_number_of_words.txt','r')
    #Initializing index
    word_count = 0
    line_count = 0

    #For loop that calculates the total sentences
    for line in num_words:
        line_count += 1
        #For loop that calculates the total words in that sentence
        for words in line.split():
            word_count += 1
            
    
    print('Average number of words per line: %.1f' %(word_count / line_count))  

#Calls main function
main()
