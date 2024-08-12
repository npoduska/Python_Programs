import colorgram, random
from turtle import Turtle, Screen

#Extract colors from a real Hirst dot painting
# numcolors = 30
color_list =[(209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190), (233, 174, 161), (141, 213, 224), (191, 191, 193), (160, 211, 182), (105, 46, 100), (8, 117, 39)]
# num_items = len(color_list)
# print(num_items)
# # Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', numcolors)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_list.append(new_color)
    
# print(color_list)

#Use these colors to create dots in 10x10 array
timmy_the_turtle = Turtle()

timmy_the_turtle.shape("arrow")
timmy_the_turtle.speed('fastest')
timmy_the_turtle.hideturtle()
# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)

num_dots = 10 #Number of dots in a row and in a column
dot_size=10
dot_spacing=20
vertical_dot_spacing = dot_spacing
for t in range(num_dots):
    #draw a horizontal line
    for i in range (num_dots):
        timmy_the_turtle.dot(dot_size,random.choice(color_list))
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(dot_spacing)
        # print(dot_color)
    timmy_the_turtle.setposition(0,vertical_dot_spacing) #Go to new vertical line
    vertical_dot_spacing = vertical_dot_spacing + dot_spacing
    
screen = Screen()
screen.exitonclick()
