################
# Author: Andrew Wang
# Date: 10/26/2019
# This programs reads the file and displays the average annual change in population, the greatest
#   increase in population, and the smallest increase in population during the time period
#################
#Main function
def main():
    #Opens and reads the file
    us_pop = open('USPopulation.txt', 'r')
    #Initializing variables
    pop_list = []
    pop_change = []
    total_pop = 0

    #For loop that puts each line into a list
    for line in us_pop:
        population = float(line)
        pop_list.append(population)

    #For loop that calculates the change of population between year and previous year
    for i in range(len(pop_list) - 1):
        pop_change.append(pop_list[i+1] - pop_list[i])
        total_pop += pop_change[i]

    #Finds the when change of population is maximum/minimum 
    pop_max = pop_change.index(max(pop_change)) + 1951
    pop_min = pop_change.index(min(pop_change)) + 1951

    print('The average annual change in population during the time period is %.2f' %(total_pop/(len(pop_list) - 1)))
    print('The year with the greatest increase in population was %.0f' %pop_max)
    print('The year with the smallest increase in population was %.0f' %pop_min)

main()
 
    
