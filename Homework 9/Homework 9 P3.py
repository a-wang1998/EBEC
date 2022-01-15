################
# Author: Andrew Wang
# Date: 11/10/2019
# This programs reads the file of gas prices for each week in 1994 and plots it
#   in a line chart and bar chart
#################
import matplotlib.pyplot as plt

#Main function
def main():
    #Opens and reads file
    gas = open('1994_Weekly_Gas_Averages.txt', 'r')
    line = gas.readlines()
    #Initializing variable
    year = []

    #For loop at reads file and put it into a list
    for i in range(len(line)):
        line[i] = line[i].rstrip('\n')
        line[i] = float(line[i])
    
    week = list(range(1, len(line) + 1))

    line_graph(week, line)
    bar_graph(week, line)

    gas.close()

#Function that plots data into line chart
def line_graph(week, line):
    plt.plot(week, line)
    plt.title('1994 Weekly Gas Prices')
    plt.xlabel('Weeks (by number)')
    plt.ylabel('Average Prices')
    plt.grid()

    plt.savefig('Q3_line.png')
    plt.show()

#Function that plots data into bar chart
def bar_graph(week, line):
    bar_width = 0.5
    colors = ('b')    
    
    plt.bar(week, line, bar_width, color=colors, align='center')
    
    plt.xlabel('Weeks (by number)')
    plt.ylabel('Average Prices')
    plt.xticks([0,10,20,30,40,50])
    plt.yticks([1,1.025,1.050,1.075,1.1,1.125,1.15])
    plt.ylim(bottom = 0.975, top = 1.17)

    plt.savefig('Q3_bar.png')
    plt.show()

#Calls main function    
main()
