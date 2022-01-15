################
# Author: Andrew Wang
# Date: 10/3/2019
# This program uses user define function allows user input 5 test scores and the program will determine
#   the letter grade of the score and the average.
#################

#Main function
def main():
    #Initialize variables
    total_score = []
    grade = []
    
    #For loop that only allows 5 input
    for i in range(5):
        total_score.append(get_valid_score())
        average = calc_average(sum(total_score))
        grade.append(determine_grade(total_score[i]))       
                       
    for i in range(5):
        print('The letter grade for %d is %c' %(total_score[i], grade[i]))
            
    print('The average test score is %.2f' %(average))
        
#User defined function which allows user to input test scores
def get_valid_score():
    count = 5
    for i in range(count):
        score = float(input('Enter a score: '))
        if score >= 0 and score <= 100:
            return score
        else:
            print('Invalid Input. Please try again')
            
        

#User defined function which calculates average of five test scores
def calc_average(total_score):
    
    average = total_score / 5

    return average

#User defined function which assigns letter grade to a score
def determine_grade(score):

    if score >= 90 and score <= 100:
        letter_grade = 'A'
    elif score >= 80 and score <= 89:
        letter_grade = 'B'
    elif score >= 70 and score <= 79:
        letter_grade = 'C'
    elif score >= 60 and score <= 69:
        letter_grade = 'D'
    elif score < 60:
        letter_grade = 'F'
    
    return letter_grade

main()
