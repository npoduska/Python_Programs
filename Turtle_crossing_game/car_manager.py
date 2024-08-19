from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] #car colors
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
        
    def __init__(self):
        self.all_cars = [] #creating list of all the cars on the screen
        self.car_speed = STARTING_MOVE_DISTANCE #initializing the starting speed of the cars.
        
    def create_car(self):  #create some cars!
        if random.randint(1,6) == 1:    #do this to slow the frequency of creating cars. Give our poor turtle a chance!
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y_position = random.randint(-250, 250)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)
        
    # move the cars from right to left side of the screen.
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    #Make the cars go faster if the turtle was able to reach the other side of the road.        
    def faster_cars(self):
        self.car_speed += MOVE_INCREMENT
        
    
