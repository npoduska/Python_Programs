"""This is the classic snake game.
    Control the snake using the up,down,left,right arrow keys.
    The snake gets longer and time goes faster after every time it eats.
    Go for the high score!
    """

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard    

import random, time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")  
screen.tracer(0)

snake =Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

time_const = 0.4
game_on = True
while game_on:
    screen.update()
    time.sleep(time_const)
    snake.move()
    
    # Detect when snake gets the food; tail gets longer, time gets faster
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        time_const = time_const /1.03
        # print(time_const)
        
    # Detect when snake touches the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.gameover()
        
    # Detect when snake eats its tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.gameover() 











screen.exitonclick()