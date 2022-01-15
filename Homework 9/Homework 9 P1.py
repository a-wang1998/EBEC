################
# Author: Andrew Wang
# Date: 11/10/2019
# This programs allows user to input sales for each month of the year and creates a pie chart
#################
import matplotlib.pyplot as plt

#Main function
def main():
    #Initializing variable
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sales = []
    color = ('r', 'g', 'b', 'y', 'm', 'w', 'k', 'blue', 'pink', 'brown', 'ivory', 'black')

    #For loop that allows user to input sales for each month
    for i in range(12):
        values = int(input('Enter the sales value of ' +month[i]+ ': '))
        sales.append(values)

    #Creates pie chart
    plt.pie(sales, labels=month, colors=color)
    plt.title('Monthly Sales Values')
    plt.savefig('Q1.png')
    plt.show()
    
#Calls main function    
main()

            
