"""This is quiz game where you type in as many US states as you can! 
    """

import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To collect the x,y coordinates on the gif image
# def get_mouse_click_coor(x,y):
#     print(x,y)  
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

turtle=turtle.Turtle()
guessed_states = []

score = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()  # Capitalize the first letter

    data = pandas.read_csv("us-states-game/50_states.csv")
    # print(data['state'])
    all_states = data['state']
    
    if answer_state == "Exit":
       # new_item=[new_item for item in list if test]
        missing_states = [state for state in all_states if state not in guessed_states]  #List comprehensioning the following 4 lines of code into just this one line.
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("us-states-game/states_to_learn.csv")
        break
    
    if answer_state in data['state'].values:
        # print("True!")    
        # print(answer_state)
        answer_state_data = data[data.state == answer_state]
        # print(answer_state_data)
        # answer_state_data_x = int(answer_state_data.x)
        # print(answer_state_data_x)
        # answer_state_data_y = int(answer_state_data.y)
        # print(answer_state_data_y)
        
        
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(answer_state_data.x.item(),answer_state_data.y.item()) 
        turtle.write(answer_state)
        turtle.home()
        
        guessed_states.append(answer_state)
        


    
            
            
    
