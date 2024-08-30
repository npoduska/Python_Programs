"""This program allows you to convert miles to kilometers in a GUI."""

from tkinter import *  #import everthing from tkinter

window = Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Setting all the labels up in the GUI
# Miles Label
miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)
#Km Label
km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)
#Is equals to Label
equals_label = Label(text="is equals to", font=("Arial", 16))
equals_label.grid(column=0, row=1)
#answer Label
answer_label = Label(text="0", font=("Arial", 16))
answer_label.grid(column=1, row=1)

# the button functionality. 
def button_clicked():
    print("Answer")
    # a_label.config(text="I got clicked yo!")
    miles_input = input.get() #Take in the input for miles
    km_output = float(miles_input)*1.609  #Convert it to kilometer as a floating point number
    answer_label.config(text = round(km_output, 2))  #Spit out the answer, rounding the number to 2 decimal places.

# Setting up the action button
button = Button(text = "Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Enter miles here
input = Entry(width = 10)
input.grid(column=1, row=0) #Can not use grid and pack in the same program! Use one or the other!




window.mainloop() #Keep the window open and forever looping though the program