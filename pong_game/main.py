"""This is the classic Pong game, hitting a ball back and forth with paddles on the left and right side of 
    the screen.
    Control the leftside paddle using the 'w' and 's' keys. 
    Control the rightside paddle using 'up arrow' and 'down arrow' keys.
    Press and holding a key doesn't continously move the paddle. You must repeatedly tap the key to move the paddle.
    When the ball goes past a paddle, the other side gets a point. The game restarts automaticly with the ball 
    going to the opposite side paddle. The ball moves a little bit faster after it hits a paddle.
    Good luck! Have fun!
    """

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

time_const = 0.1
game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(time_const)
    
    # Detect when ball hits the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()
        
    # Detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time_const = time_const /1.03
        
    # Detect if ball misses the rightside paddle
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()
        time_const = 0.1
        
    # Detect if ball misses the leftside paddle
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()
        time_const = 0.1

screen.exitonclick()


