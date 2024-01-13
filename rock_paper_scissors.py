import random

# Notes:
#     0 = Rock
#     1 = Paper
#     2 = Scissors
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

# ASCII art:
fist=('''
  .----.-----.-----.-----.
 /      \     \     \     \
|  \/    |     |   __L_____L__
|   |    |     |  (           \
|    \___/    /    \______/    |
|        \___/\___/\___/       |
 \      \     /               /
  |                        __/
   \_                   __/
    |        |         |
    |                  |
    |                  |''')

paper_hand=('''      
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
              jgs    |    |''')

hand_scissors = ('''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

VK''')

# Player's inputs
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

# Check for invalid inputs
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")

# Check who wins
if user_choice == 0:
    print("Your choice:")
    print(fist)
    if computer_choice == 0:
        print("Computer's choice:")
        print(fist)
        print("Draw! Replay again!")
    if computer_choice == 1:
        print("Computer's choice:")
        print(paper_hand)
        print("Computer wins!")
    if computer_choice == 2:
        print("Computer's choice:")
        print(hand_scissors)
        print("You win!")
if user_choice == 1:
    print("Your choice:")
    print(paper_hand)
    if computer_choice == 0:
        print("Computer's choice:")
        print(fist)
        print("You win!")
    if computer_choice == 1:
        print("Computer's choice:")
        print(paper_hand)
        print("Draw! Replay again!")
    if computer_choice == 2:
        print("Computer's choice:")
        print(hand_scissors)
        print("Computer wins!")
if user_choice == 2:
    print("Your choice:")
    print(hand_scissors)
    if computer_choice == 0:
        print("Computer's choice:")
        print(fist)
        print("Computer wins!")
    if computer_choice == 1:
        print("Computer's choice:")
        print(paper_hand)
        print("You win!")
    if computer_choice == 2:
        print("Computer's choice:")
        print(hand_scissors)
        print("Draw! Replay again!")
