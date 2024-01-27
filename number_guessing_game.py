# Need this to generate a random integer
import random

# Setting a flag to keep the game playing over and over again.
keep_playing = True

# This is the master loop that keeps the game going. As long as keep_playing is True, the game will go on.
while keep_playing:
    # Setting up the intro and initial values.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'e' for easy, or 'h' for hard: ")
    
    # Get a random number.
    random_num = random.randint(1,100)
    # Uncomment the following line if you want to cheat.
    # print(random_num)
    
    # Setting number of tries corresponding with easy or hard levels of play.
    if level == "e":
        tries = 10
    else:
        tries = 5
    
    # Let the player keep guessing the number as long as they have number of attempts left.
    while tries > 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        if guess_num < random_num:
            print("Too low.")
            tries = tries - 1
        elif guess_num > random_num:
            print("Too high.")
            tries = tries - 1
        elif guess_num == random_num and tries > 0:
            print(f"You guessed it! The number was: {random_num}.")
            break
    if tries == 0:
        print(f"You lose. No more attempts. The number was: {random_num}")

    # Check if the player wants to play the game again.
    if input("Do you want to play again? Type 'y' or 'n': ") == "y":
        # Clear the console and play the game again
        print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
        # play_game()
    else:
        keep_playing = False