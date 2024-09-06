"""This program is supposed to be a flash card app game to help learn Polish language, but it could be easily 
modified to learn any other subject.
If you know a word or the item on the front of the card, hit the checkmark, then it will show the answer on the 
backside. That word then gets sent to a file to keep track of words that you already know, so it won't show
you them repeatedly. If you don't know the word, hit the red button (X) and it will show what the answer is, and 
it will keep that word in the stash to show you again later on.
The timer could be turned on so the card turns over in 3 seconds. It is disabled for now. 
*Some performance improvements could be made in the future...
"""

from tkinter import *  #import everthing from tkinter
import pandas, random

# Setting up blanks arrays to initialize
current_card = {} #Data to be displayed on a card
to_learn = {} #Keep track of what words a person does NOT know

try:
    polish_word_data = pandas.read_csv("Flash_Card_Project\\data\\words_to_learn.csv") #Bring in the data from the words not known list.
except FileNotFoundError:
    original_data = pandas.read_csv("Flash_Card_Project\\data\\Polish_words.csv") #Bring in the data from the CSV file that has the original list of words. This is the whole dictionary.
    to_learn = original_data.to_dict(orient="records") #Send this dictionary list to the to_learn array even if this error occurs.
else:
    to_learn = polish_word_data.to_dict(orient="records") #Load up the to_learn list.



# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- RANDOM WORD COLLECTOR ------------------------------- #
def random_words():
    global current_card, flip_timer
    
    window.after_cancel(flip_timer) #Flips the card over, and restarts the countdown timer.
    
    current_card = random.choice(to_learn) #Pick a random pair of words from the to_learn list.
    current_card["Polish"] #Get the Polish word
    # print(current_card)
    canvas.itemconfig(language_label, text="Polish", fill='black')
    canvas.itemconfig(word_label, text=current_card["Polish"], fill='black') #Display the current Polish word on the front of the card.
    canvas.itemconfig(card_background, image = card_img) #Display the front of the card image.
    
    flip_timer = window.after(3000, func= flip_card) #Flip the card to the backside (answer side) after 3 seconds.
    
# ---------------------------- FLIP CARD ------------------------------- #
def flip_card(): #This function flips the card over to the backside to show the answer.
    canvas.itemconfig(language_label, text="English", fill= 'white')
    canvas.itemconfig(word_label, text=current_card["English"])
    canvas.itemconfig(card_background, image = back_card_img)
    
# ---------------------------- STORE KNOWN TERMS ------------------------------- #
def is_known(): #This function stores words not known yet to its own list, so when you start the app over again, it already knows which words to NOT show.
    to_learn.remove(current_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("Flash_Card_Project\\data\\words_to_learn.csv", index=False) #Store words in this file. Index=False disables assigning an index number to each word pair. This would clutter up the list after multiple restarts of the app.
    
    flip_card() #Flip card over function
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
# window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) 

flip_timer = window.after(3000, func= flip_card)

canvas = Canvas(width=800, height=526)
card_img = PhotoImage(file="Flash_Card_Project\\images\\card_front.png")
back_card_img = PhotoImage(file="Flash_Card_Project\\images\\card_back.png")
card_background = canvas.create_image(400,263, image = card_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Language Label
language_label = canvas.create_text(400, 150,text="", font=("Ariel", 30, "italic"))
# The Word Label
word_label = canvas.create_text(400, 263,text="", font=("Ariel", 45, "bold"))

# Setting up wrong button
x_image = PhotoImage(file="Flash_Card_Project\\images\\wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, command = random_words)
wrong_button.grid(column=0, row=1)
# Setting up correct button
checkmark_image = PhotoImage(file="Flash_Card_Project\\images\\right.png")
correct_button = Button(image=checkmark_image, highlightthickness=0, command = is_known)
correct_button.grid(column=1, row=1)

random_words()
    
window.mainloop() #Keep the window open and forever looping though the program