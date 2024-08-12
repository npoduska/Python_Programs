from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")

#drawing a square
#for i in range(4):
#    timmy_the_turtle.forward(200)
#    timmy_the_turtle.right(90)

#draw a dashed line
#for i in range (15):
#    timmy_the_turtle.pendown()
#    timmy_the_turtle.forward(10)
#    timmy_the_turtle.penup()
#    timmy_the_turtle.forward(10)

"""
#drawing shapes
sides = 3

# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)

for i in range(6):
    angle = 360/sides
    for j in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
    sides += 1
    #pick a random color for the line
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy_the_turtle.pencolor((r,g,b))
    """

"""
#Doing a random walk
# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)
timmy_the_turtle.pensize(10)
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed(10)

for i in range(100):
    #pick a random color for the line
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy_the_turtle.pencolor((r,g,b))
    
    rand_i = random.randint(0, 3)
    timmy_the_turtle.setheading(90*rand_i)
    timmy_the_turtle.forward(20)
"""

#Drawing a spirograph
# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)
#timmy_the_turtle.pensize(10)
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed('fastest')

for i in range(300):
    #pick a random color for the line
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy_the_turtle.pencolor((r,g,b))
    
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(360/(i+1))

screen = Screen()
screen.exitonclick()
