################
# Author: Andrew Wang
# Date: 10/3/2019
# This program uses turtle graphics with a loop and drasws a Start Pattern with a user input number of corners
#################

import turtle

#Allows user to input amount of corners
corners = int(input('Enter the number of corners: '))

#Calculation of angle 
angle = 360 / corners

#Setting up turtle
turtle.setup(2000,2000)
turtle.pencolor('red')
turtle.fillcolor('green')
turtle.goto(0,0)
turtle.begin_fill()

#For loop that draws the shape from 0 to corner - 1
for i in range(0, corners):
    turtle.setheading(i * (180 - angle))
    turtle.forward(200)
    
turtle.setheading(0)

turtle.end_fill()
turtle.done()
