"""This is a fun turtle race game. The user bets on 1 of the 6 colored turtles to win, then just like a horse 
    race, they race across the screen at random paces. Whichever turtle gets to the edge of the screen first,
    WINS! And the user wins if they picked the right turtle to win.
    """

from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors=["red", "blue", "orange", "yellow", "green", "purple"] #turtle colors

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Type red, blue, orange, yellow, green, or purple color: ")

#check user input
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt = "That is not a color of a turtle. Type red, blue, orange, yellow, green, or purple color:")

y_pos=-60 #initial position of the first turtle

all_turtles = [] #list of all the turtles competing

#create some turtles!
for turtles in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles])
    new_turtle.goto(x = -230, y = y_pos)
    y_pos = y_pos+20
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You picked a winner! The winning color was the {winning_color} turtle!")
            else:
                print(f"You lose! The winning turtle was {winning_color} color.")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    
screen.exitonclick()