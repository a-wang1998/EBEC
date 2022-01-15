
def survey():
    survey_file = open('survey.txt', 'r')
    line = survey_file.readlines()
    survey_list = []
    
    for i in range(len(line)):
        line[i] = line[i].rstrip('\n')
        #survey_list.extend(line[i].spilt())

    print(line)

survey()
