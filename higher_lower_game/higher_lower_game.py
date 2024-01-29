import random
from game_data import data
import art

# print(data[1])
# person_a = data[1]
# print(person_a.get("name"))
# print(person_a.get("follower_count"))
# print(person_a.get("description"))
# print(person_a.get("country"))

def get_random_person():
    # bring in data here
    # Pick a random person from the data set
    return random.choice(data)

def is_larger(person_a_follower, person_b_follower): 
    if person_a_follower > person_b_follower:
        return "a"
    else:
        return "b"

# Program start here**************************************************************
print(art.logo)

# call get_random_person to get our first and second person
person_a = get_random_person()
score = 0
keep_playing = True

while keep_playing:
    person_a_name = (person_a.get("name"))
    person_a_follower = (person_a.get("follower_count"))
    person_description = (person_a.get("description"))
    person_country = (person_a.get("country"))

    # # logo
    print(f"Compare A: {person_a_name}, a {person_description}, from {person_country}.")

    # # vs. logo
    print(art.vs)

    person_b = get_random_person()
    # check if person a is the same as person b
    while person_a == person_b:
        # Get a new person b
        person_b = get_random_person(data)
        
    person_b_name = (person_b.get("name"))
    person_b_follower = (person_b.get("follower_count"))
    person_description = (person_b.get("description"))
    person_country = (person_b.get("country"))
    print(f"Against B: {person_b_name}, a {person_description}, from {person_country}.")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # compare number of followers. If the user guesses the correct person with greater number of followers,
    # they win. Score goes up +1, previous person goes to 'A', and a random person gets picked as person B.
    
    if user_guess == is_larger(person_a_follower, person_b_follower):
        score = score + 1
        print(f"You're right! Current score: {score}.")
        person_a = person_b
    else:
        print(f"You lose. Current score: {score}.")
        print(f"{person_a_name} has {person_a_follower} followers, and {person_b_name} has {person_b_follower} followers.")
        keep_playing = False

    # The user is prompted to guess again.
    # This repeats until user is wrong, then game over.
    # Clear the console and play again
    # print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")    