################
# Author: Andrew Wang
# Date: 9/29/2019
# This program uses turtle graphs and draws 5 different colored circle at different locations
#################

#Initializes turtle graphics and draws blue circle
import turtle
turtle.setup(2000, 2000)
turtle.pensize(10)
turtle.pencolor('blue')
turtle.circle(50)

#Draws yellow circle
turtle.penup()
turtle.goto(62.5,-50)
turtle.pendown()
turtle.pencolor('yellow')
turtle.circle(50)

#Draws black circle
turtle.penup()
turtle.goto(125,0)
turtle.pendown()
turtle.pencolor('black')
turtle.circle(50)

#Draws green circle
turtle.penup()
turtle.goto(187.5,-50)
turtle.pendown()
turtle.pencolor('green')
turtle.circle(50)

#Draws red circle and terminates turtle
turtle.penup()
turtle.goto(250,0)
turtle.pendown()
turtle.pencolor('red')
turtle.circle(50)
turtle.done()
