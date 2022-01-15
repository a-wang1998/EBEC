################
# Author: Andrew Wang
# Date: 10/13/2019
# This program that draws a snowman using turtle.
#################
import turtle

#Main function
def main():
    turtle.speed(0)
    
    drawBase()
    drawMidSection()
    drawHead()
    drawHat()
    drawArms()

#This function draw the base of the snowman
def drawBase():
    turtle.penup()
    turtle.goto(0,-160)
    turtle.pendown()
    turtle.circle(80)

#This function draws the middle snowball
def drawMidSection():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(60)

#This function draws the two arms
def drawArms():
    #Right arm
    turtle.penup()
    turtle.goto(60,60)
    turtle.pendown()
    turtle.left(20)
    turtle.forward(30)
    turtle.right(20)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(45)
    turtle.forward(15)
    turtle.right(45)

    #Left arm
    turtle.penup()
    turtle.goto(-60,60)
    turtle.pendown()
    turtle.right(20)
    turtle.backward(30)
    turtle.left(130)
    turtle.forward(20)
    turtle.left(20)
    turtle.forward(15)
    turtle.backward(15)
    turtle.right(25)
    turtle.forward(15)
    turtle.right(105)

#This function draws the head, eyes, and mouth
def drawHead():
    #Draws head
    turtle.penup()
    turtle.goto(0,120)
    turtle.pendown()
    turtle.circle(40)

    #Draws eyes
    turtle.penup()
    turtle.goto(20,170)
    turtle.pendown()
    turtle.circle(5)
    
    turtle.penup()
    turtle.goto(-20,170)
    turtle.pendown()
    turtle.circle(5)

    #Draws mouth
    turtle.penup()
    turtle.goto(-20,140)
    turtle.pendown()
    turtle.forward(40)  

#This function draws the hat
def drawHat():
    turtle.fillcolor('black')
    turtle.penup()
    turtle.goto(-60,180)
    turtle.pendown()
    turtle.begin_fill()
    
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    
    turtle.end_fill()
    
main()
