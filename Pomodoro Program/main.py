"""This is a pomodoro timer program. Get ready to get stuff done!
    Hit the start button, work for 25 minutes, then you get 5 minutes break. It repeats this 8 times 
    then you get a long 20 minute break. 
    Hit reset to the timing sequence over again.
    """

import math
from tkinter import *  #import everthing from tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_MIN = 1
# SHORT_BREAK_MIN = 1
# LONG_BREAK_MIN = 1.1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    
    #Can only hit the button once, else, the program acts not as advertised.
    start_button.config(state='normal')
    reset_button.config(state='disabled')
    
    window.after_cancel(timer) #Stop timer
    
    # timer text back to 00:00
    canvas.itemconfig(timer_text, text = "00:00")
    #Label set back to "Timer"
    main_label.config(text = "Timer")
    #Reset number of checkmarks shown
    checkmarks_label.config(text = "")
    
    # Reps are steps you are in within the pomodoro counting process.
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    #Can only hit the button once, else, the program acts screwy.
    start_button.config(state='disabled')
    reset_button.config(state='normal')
    
    global reps
    reps += 1
    # print(reps)
    
    # Need time in seconds.
    work_seconds = WORK_MIN *60
    short_break_seconds = SHORT_BREAK_MIN *60
    long_break_seconds = LONG_BREAK_MIN *60
    
    # If it's the 8th rep...
    if reps % 8 == 0:
        countdown(long_break_seconds)
        main_label.config(text="Break time!", fg=RED, font=(FONT_NAME, 36), bg=YELLOW)
    # If it's the 2nd/4th/6th rep...
    elif reps % 2 ==0:
        countdown(short_break_seconds)
        main_label.config(text="Break time!", fg=PINK, font=(FONT_NAME, 36), bg=YELLOW)
    else:
        # If it's the 1st/3rd/5th/7th rep...
        countdown(work_seconds)
        main_label.config(text="Work time!", fg=GREEN, font=(FONT_NAME, 36), bg=YELLOW)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # Start the timer with the pomopdoro window wherever it naturaly is.
    window.attributes('-topmost', False)


    count_minute = math.floor(count / 60) #Only need minutes figure. Ex, 4:55 is rounded to just 4.
    count_seconds = count % 60 #Need just the seconds component.
    
    #This part is for the timer to display 0:07, rather then 0:7
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    # This part brings the pomodoro program window to the top of all the other programs currently running on the computer when counter gets to 5seconds left.
    if count == 5:
        window.attributes('-topmost', True)
    
    # Show timer text    
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    
    # Keep the count positive, no negative figures here.
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count-1 )
    else:
        start_timer()
        mark = "" #This is for the checkmarks displayed after every cycle.
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"  #Add a checkmark
        checkmarks_label.config(text = mark)
            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold") )
canvas.grid(column=1, row=1)

# Main Timer Label
main_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36), bg=YELLOW)
main_label.grid(column=1, row=0)
# Checkmark Label
checkmarks_label = Label(fg=GREEN, font=(FONT_NAME, 16, "bold"), bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

# Setting up the start button
start_button = Button(text = "Start", highlightthickness=0, command = start_timer)
start_button.grid(column=0, row=2)
# Setting up the reset button
reset_button = Button(text = "Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop() #Keep the window open and forever looping though the program