################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs read the file and calcualtes the average number of steps taken for each month in the file.
#################
#Main function
def main():
    #Reads the file
    steps = open('steps.txt', 'r')
    #Reads the line of the file
    line = steps.readline()
    #List for months and number of days for each month
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    average = []

    #For loop that adds the total number of steps and calculates the average
    for i in range(len(days)):
        total_amt = 0
        #For loop that adds the total number of steps for each number of days
        for j in range(days[i]):
            step_amt = float(line)
            total_amt += step_amt
            line = steps.readline()
            
        average.append(total_amt / days[i])
        print('The average steps taken in ' +month[i]+ ' was',format(average[i], ',.1f'))

#Calls main function
main()
