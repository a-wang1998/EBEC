################
# Author: Andrew Wang
# Date: 11/03/2019
# This programs reads two different text files and compares in different ways as in the frequency of each words,
#   the words that appears in both files, and the words that appear in either file but not both.
#################
#Main function
def main():
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word_set1 = xian1(punc)
    word_set2 = xian2(punc)
    commonandeither(word_set1, word_set2)

#Function that reads xian1.txt
def xian1(punc):
    #Opens and reeads the file
    xian_1 = open('xian_1.txt', 'r',encoding='utf8',errors="ignore")
    out_file1 = open('word_freqeuncy_1.txt', 'w')
    line1 = xian_1.readlines()

    #Initializing variable
    word_list1 = []
    word_set1 = set()
    word_dir1 = {}

    #For loop that removes punctuation, changes to lowercase, and put sentence into a list
    for i in range(len(line1)):
        line1[i] = line1[i].rstrip('\n')
        line1[i] = line1[i].lower()
        for word in punc:
            line1[i] = line1[i].replace(word, '')

    #For loop that get a single list with all the words in the file
    for i in range(len(line1)):
        current_line = line1[i].split()
        word_list1.extend(current_line)
    word_set1.update(word_list1)

    #For loop that gets unique word set in the file
    for key in word_set1:
        count = word_list1.count(key)
        word_dir1[key] = count
    
    #For loop that get directiory which keys is words and value is frequency of the word 
    out_file1.write('Word: Frequency\n')
    for key in word_dir1:
        current_line = key + ': ' + str(word_dir1[key]) + '\n'
        out_file1.write(current_line)

    xian_1.close()
    out_file1.close()

    return word_set1

#Function that reads xian2.txt
def xian2(punc):
    #Opens and reeads the file
    xian_2 = open('xian_2.txt', 'r',encoding='utf8',errors="ignore")
    out_file2 = open('word_freqeuncy_2.txt', 'w')
    line2 = xian_2.readlines()

    #Initializing variable
    word_list2 = []
    word_set2 = set()
    word_dir2 = {}

    #For loop that removes punctuation, changes to lowercase, and put sentence into a list
    for i in range(len(line2)):
        line2[i] = line2[i].rstrip('\n')
        line2[i] = line2[i].lower()
        for word in punc:
            line2[i] = line2[i].replace(word, '')

    #For loop that get a single list with all the words in the file
    for i in range(len(line2)):
        current_line = line2[i].split()
        word_list2.extend(current_line)
    word_set2.update(word_list2)

    #For loop that gets unique word set in the file
    for key in word_set2:
        count = word_list2.count(key)
        word_dir2[key] = count    

    #For loop that get directiory which keys is words and value is frequency of the word 
    out_file2.write('Word: Frequency\n')
    for key in word_dir2:
        current_line = key + ': ' + str(word_dir2[key]) + '\n'
        out_file2.write(current_line)

    xian_2.close()
    out_file2.close()

    return word_set2

#Function that finds the common_words and eitherbutnotboth
def commonandeither(word_set1, word_set2):
    
    #Finds intersection and symmetric difference 
    common_words = word_set1 & word_set2
    eitherbutnotboth = word_set1 ^ word_set2

    #Creates file for writing
    common_file = open('common_words.txt', 'w')
    either_file = open('eitherbutnotboth.txt', 'w')

    #For loop that writes common_words into file
    for i in common_words:
        common_file.write(str(i) + '\n')
        
    #Writes eitherbutnotboth into file
    either_file.write(str(eitherbutnotboth))
    
    common_file.close()
    either_file.close()

#Calls main function
main()    

  
