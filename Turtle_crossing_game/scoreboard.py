from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.level = 0
            self.color("black")
            self.penup()
            self.goto(-280,260)
            self.hideturtle()
            self.update_scoreboard()
        
        def level_up(self):
            self.level += 1
            self.clear()
            self.update_scoreboard()
            
        def update_scoreboard(self):
            self.write(f"Level: {self.level}", align = "left", font = FONT )
            
        def gameover(self):
            self.goto(0,0)
            self.write(f"Game Over. Splat!!", align = "center", font = FONT )
            
