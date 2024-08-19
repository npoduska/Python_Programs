"""This is a fun game of a turtle trying to cross the road without getting hit by a car, like the classic game 'Frogger'.
    The turtle can only go forward with the 'Up' key, no backwards. 
    Get to the other side of the road to get a high score!
    Each level gets harder! Watch out for the cars!
    """

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

#Some constants to start things off...
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)

screen.listen()
screen.onkey(player.move_forwards, "Up")
    
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect when turtle gets hit by car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
            
    #Whenever the turtle reaches the other side of the road, Level up and restart turtle. Oh, and the cars go faster!
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.level_up()
        player.goto(STARTING_POSITION)
        car_manager.faster_cars()
    
    










screen.exitonclick()