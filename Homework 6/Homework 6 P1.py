################
# Author: Andrew Wang
# Date: 10/20/2019
# This programs allows the user to enter the total rainfall for an year into a list,
#   and the program will calcaulate the average rainfall, total rainfall, and months with the
#   highest and lowest rainfall
#################
#Creating two lists
rainfall = [0] * 12
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#For loop that allows user to input 12 month of rainfall
for i in range(len(rainfall)):
    rainfall[i] = float(input('Enter the rainfall for ' +month[i]+ ': '))

#Calculation of total and average rainfall
total_rain = sum(rainfall)
avg_rain = sum(rainfall) / 12
print('Total rainfall: %.2f' %total_rain)
print('Average rainfall: %.2f' %avg_rain)

#Finding the month of highest and lowest rainfall
high_month = rainfall.index(max(rainfall))
low_month = rainfall.index(min(rainfall))

print('Highest rainfall: ' +month[high_month])
print('Lowest rainfall: ' +month[low_month])
