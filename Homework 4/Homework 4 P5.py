################
# Author: Andrew Wang
# Date: 10/3/2019
# This program uses durtle graphics to draw a Hypnotic Pattern with width between two rings as 10.
#################

import turtle

#Initialize variable
index = 1

#Setting up turtle
turtle.pencolor('black')
turtle.forward(1)
turtle.setheading(90)
turtle.forward(1)

#While loop that increases length by 10 for each side
while index <= 48:
    
    turtle.setheading(90)
    turtle.forward(10*index)
    index += 1
    turtle.setheading(180)
    turtle.forward(10*index)
    index += 1
    turtle.setheading(270)
    turtle.forward(10*index)
    index += 1
    turtle.setheading(0)
    turtle.forward(10*index)
    index += 1

turtle.setheading(90)
turtle.forward(10*49)

turtle.done()
