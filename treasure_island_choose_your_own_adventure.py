# https://ascii.co.uk/art
print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
''')
# Intro
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

# First decision to make.
input1 = input('Type "left" or "right".\n').lower()
# If they picked anything other then 'right', game over.
if input1 != "left":
    print("Fall into a hole. Game Over!")
else:
    # Continue with the game
    print("You've come to a lake. There is an island in the middle of the lake.")
    input2 = input('Do you want to swim or wait? Type "swim" or "wait".\n').lower()
    if input2 != "wait":
        print("You got attacked by an angry trout. Game Over!")
    else:
        # 3 doors to pick from, 4 possible decisions to make...
        print("You've arrived at the island unharmed. There is house with 3 doors. One red, one yellow, and one blue.")
        input3 = input('Which door do you choose? Type "red" or "blue" or "yellow".\n').lower()
        if input3 == "red":
            print("Burned by fire. Game Over!")
        if input3 == "blue":
            print("Eaten by beasts. Game Over!")
        if input3 == "yellow":
            print("You Win!!!")
        else:
            print("You picked a door that doesn't exist. Game Over.")