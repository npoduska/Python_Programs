"""This is an etch-a-sketch game. 
Control the arrow using "W","A","S","D" keys to draw a picture, just like on the
etch-a-sketch game!"""

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clear():
    new_heading = tim.heading()-10
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
