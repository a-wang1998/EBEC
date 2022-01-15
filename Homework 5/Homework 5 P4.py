################
# Author: Andrew Wang
# Date: 10/13/2019
# This program that draws a checkboard which the user inputs the number of squares in each side
#################
import turtle

#Main function
def main():
    sides = int(input('Enter the number of squares in one side: '))
    turtle.setup(1000,1000)
    turtle.speed(0)
    width = 20

    #For loop that determines the x-coordinate
    for i in range(sides):
        x = i*width

        #For loop that determines the y-coordinate
        for j in range(sides):
            y = -j*width

            #If statement that determines which square is filled with back or white
            if j % 2 == 0 and i % 2 == 0:
                color = 'black'
            elif i % 2 != 0 and j % 2 != 0:
                color = 'black'
            else:
                color = 'white'
                
            drawSquare(x,y,width,color)
    
#This function that draws a square with corresponding x,y position, width, and color.
def drawSquare(x,y,width,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    #For loop that draws the square
    for i in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
    
main()
