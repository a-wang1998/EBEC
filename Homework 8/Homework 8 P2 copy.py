################

# Author: Jennifer Lo

# Date: 10/26/2019

# This program takes two files and compare the two files

#################
#all punctuations that may occur in the text file
punctuations = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
dict1 = {} ##dictionary for word frequency 1
dict2 = {} ##dictionary for word frequency 2
dict3 = {} ##dictionary for common words
dict4 = {} ##dictionary for either but not both
## open two files
file1 = open("xian_1.txt", encoding="utf-8")
file2 = open("xian_2.txt", encoding="utf-8")

## add words to dictionary
for line in file1:
    for word in line.split():
        ## make the word in lower case
        word = word.lower()
        ## remove punctuation
        for x in word:
            if x in punctuations:
                word = word.replace(x,"")
        ## update dictionary
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
## add words to dictionary
for line in file2:
    for word in line.split():
        ## make the word in lower case
        word = word.lower()
        ## remove punctuation
        for x in word:
            if x in punctuations:
                word = word.replace(x,"")
        ## update dictionary
        if word not in dict2:
            dict2[word] = 1
        else:
            dict2[word] += 1
## add word to dictionary "both" and "either"
for key in dict1:
    if key in dict2:
        dict3[key] = 1
        dict4[key] = 0
    else:
        dict3[key] = 0
        dict4[key] = 1
#write to output file word frequency1
fileout1 = open("word_frequency_1.txt","w")
fileout1.writelines("Word: Frequency\n")
for key in dict1:
    fileout1.writelines(key+': '+str(dict1.get(key))+"\n")
#write to output file word frequency2
fileout2 = open("word_frequency_2.txt","w")
fileout2.writelines("Word: Frequency\n")
for key in dict2:
    fileout2.writelines(key+': '+str(dict2.get(key))+"\n")
#write to output file common words
fileout3 = open("common_words.txt", "w")
for key in dict3:
    if(dict3.get(key) == 1):
        fileout3.writelines(str(key)+"\n")
#write to output file either but not both
fileout4 = open("eitherbutnotboth.txt", "w")
for key in dict4:
    if(dict4.get(key) == 1):
        fileout4.writelines(str(key)+"\n")

#close files
file1.close()
fileout1.close()
file2.close()
fileout2.close()
fileout3.close()
fileout4.close()

