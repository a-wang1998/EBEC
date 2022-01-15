################
# Author: Andrew Wang
# Date: 10/3/2019
# This program uses user define function that accepts an object’s falling time (in seconds)
#   as an argument and calls the function in a loop from 1 sec to 10 sec.
#################

#Main function
def main():
    #Time (s)
    time = 1
    print('Time(s) Falling Distance(m)')
    print('-----------------------------')

    #While loop that increments time by 1 until 10
    while time <= 10:
            #Inputs time and returns falling distancce
            d = falling_distance(time)
            print ('%d\t%.2f' %(time, d))
            time = time + 1
            
#User defined function for calculating falling distance
def falling_distance(time):
    #Graititional constant
    g = 9.8
    #Calculation of falling distance
    d = 0.5 * g * (time ** 2)

    #Return calculation of distance   
    return d

main()
