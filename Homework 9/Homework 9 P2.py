################
# Author: Andrew Wang
# Date: 11/10/2019
# This programs reads the file of US population during 1950 - 1990 and plots it
#   in a line chart and bar chart
#################
import matplotlib.pyplot as plt

#Main function
def main():
    #Opens and reads file
    gas = open('USPopulation.txt', 'r')
    line = gas.readlines()
    #Initializing variable
    year = []

    #For loop that reads file and put it into a list
    for i in range(len(line)):
        line[i] = line[i].rstrip('\n')
        line[i] = float(line[i])
    
    year = list(range(1950, len(line) + 1950))
    
    line_graph(year, line)
    bar_graph(year, line)

    gas.close()

#Function that plots data into line chart
def line_graph(year, line):
    plt.plot(year, line)
    plt.title('U.S. Population from 1950 to 1990')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid()
    plt.xticks([1950,1960,1970,1980,1990])
    plt.yticks([150000, 170000, 190000, 210000, 230000, 250000], ['150M', '170M', '190M', '210M', '230M', '250M'])
    
    plt.savefig('Q2_line.png')
    plt.show()

#Function that plots data into bar chart
def bar_graph(year, line):
    bar_width = 0.5
    colors = ('b')   

    plt.bar(year, line, bar_width, color=colors, align='center')
    plt.title('U.S. Population from 1950 to 1990')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks([1950,1960,1970,1980,1990])
    plt.yticks([150000, 170000, 190000, 210000, 230000, 250000], ['150M', '170M', '190M', '210M', '230M', '250M'])
    
    plt.ylim(bottom = 150000, top = 250000)
    plt.xlim(left = 1948, right = 1992)

    plt.savefig('Q2_bar.png')
    plt.show()
    
#Calls main function
main()
