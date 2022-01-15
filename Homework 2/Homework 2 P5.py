################
# Author: Andrew Wang
# Date: 9/19/2019
# This program allows the user to input velocity, diameter of the pipe, and temperature which the program
#   will use it to calculate Reynolds Number which is used in fluid mechanics.
#################

#user input velocity
velocity = float(input('Please input velocity: '))
#user input diameter of the pipe
diameter = float(input('Please input diameter of the pipe: '))
#user input temperature
temperature = float(input('Please input tempeature (5°C, 10°C ,15°C only): '))

#if statement which calculates Renyolds Number according to different temperature.
if temperature == 5:
    kin_visc = 1.49e-6
    Re_num = (velocity * diameter) / kin_visc
    print('The Reynolds number for a flow at a speed of '+str(velocity)+ ' m/s in a pipe with '+str(diameter)+' m diameter @ '+str(temperature)+'°C is {:.2e}' .format(Re_num))

elif temperature == 10:
    kin_visc = 1.31e-6
    Re_num = (velocity * diameter) / kin_visc
    print('The Reynolds number for a flow at a speed of '+str(velocity)+ ' m/s in a pipe with '+str(diameter)+' m diameter @ '+str(temperature)+'°C is {:.2e}' .format(Re_num))


elif temperature == 15:
    kin_visc = 1.15e-6
    Re_num = (velocity * diameter) / kin_visc
    print('The Reynolds number for a flow at a speed of '+str(velocity)+ ' m/s in a pipe with '+str(diameter)+' m diameter @ '+str(temperature)+'°C is {:.2e}' .format(Re_num))
