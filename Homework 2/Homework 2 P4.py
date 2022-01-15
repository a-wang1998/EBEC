################
# Author: Andrew Wang
# Date: 9/19/2019
# This program allows the user to input total number of seconds and the program
#   will convert total amount of time into days, hours, minutes, and seconds
#################

#user input total amount of seconds
seconds = float(input('Please enter a number of seconds: '))
#60 seconds in a minute
minutes = 60

#if statement to determine the total number of seconds and calculate days, hours, minutes, and seconds accordingly
if seconds < 60:
    print('The number of seconds is less than one minute')

elif seconds >= 60 and seconds < 3600:
    minute_calc = seconds // minutes
    second_calc = seconds % minutes
    print('%.0f seconds equal to: %.0f full minute(s) and %.0f second(s).' % (seconds, minute_calc, second_calc))

elif seconds >= 3600 and seconds < 86400:
    hour_calc = seconds // (minutes * minutes)
    minute_calc = seconds % (minutes * minutes) // minutes
    second_calc = seconds % minutes
    print('%.0f seconds equal to: %.0f full hour(s), %.0f full minute(s) and %.0f second(s).' % (seconds, hour_calc, minute_calc, second_calc))

elif seconds >= 86400:
    day_calc = seconds // (minutes * minutes * 24) 
    hour_calc = seconds % (minutes * minutes * 24) // (minutes * minutes)
    minute_calc = seconds % (minutes * minutes * 24) % (minutes * minutes) // minutes
    second_calc = seconds % minutes
    print('%.0f seconds equal to: %.0f full day(s), %.0f full hour(s), %.0f full minute(s) and %.0f second(s).' % (seconds, day_calc, hour_calc, minute_calc, second_calc))
                           
