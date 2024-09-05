"""This program saves your login credentials needed for different websites.
The program can also generate a random password for you if you want. 
And once that random password is generated, it is automatically copied to clipboard for you to paste into the website form.
The website, email/username, and password info is saved in a json file.
"""

from tkinter import *  #import everthing from tkinter
from tkinter import messagebox
from random import choice, shuffle, randint 
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #------------------This function creates a random password-----------------------
    
    #The dictionary to choose letter, numbers, and symbols from
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Collecting random letters, symbols, and numbers from the dictionary using list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    #Putting all those letters, numbers, and symbols together
    password_list = password_letters + password_symbols + password_numbers
    
    #Rearrange the order of the letters, numbers, and symbols
    shuffle(password_list)

    #Joining the whole string together
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    #Generated password output. 
    # print(f"Your password is: {password}") #Print it to confirm if you want.
    password_entry.insert(0, password) #Inserts it into the password entry field
    pyperclip.copy(password ) #Automatically copies password to clipboard, ready to paste in the website or where ever you want.
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    
    #Collecting the entries inputed
    website = website_entry.get().lower()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email:": email_username,
        "password:": password,
    }}
    # Make sure all entry boxes have been filled in
    if len(website)==0 or len(email_username)==0 or len(password)==0:  # This will be True if there is an empty string
        messagebox.showinfo(title="Entry field error", message="Please do not leave any fields empty!")
    else:        
        #Messagebox confirming entry
        # is_ok = messagebox.askokcancel(title=website, message = f"These are the details entered: \nEmail: {email_username}\n Password: {password}\n Is it ok to save?")
        # print(website) #Testing purposes only!
        try:
        # if is_ok: #If all entry boxes have been filled in & info is confirmed, do the following stuff...
            #Write to file
            with open("Password_Manager/data.json", "r") as file: #Open file in read mode
                # file.write(f"{website} | {email_username} | {password}\n") 
                # json.dump(new_data, file, indent=4) #Writing to json file instead of a text file
                data = json.load(file) #Reading data from json file
                # print(data)
        except FileNotFoundError: #Do this if file has not been created yet.
            with open("Password_Manager/data.json", "w") as file: #Open file in write mode
                json.dump(new_data, file, indent=4) #Writing to new json file
        else: #Do this if there are no errors flagged
            data.update(new_data)  #Appending or adding data to json file
            
            with open("Password_Manager/data.json", "w") as file: #Open file in write mode
                json.dump(data, file, indent=4)
        finally:        
            #Delete the entries in the Website and password entry fields. Can keep the email field alone.
            website_entry.delete(0,'end')
            password_entry.delete(0, 'end')
            website_entry.focus()
# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    #Collecting the entries inputed
    website = website_entry.get().lower()
    
    if len(website)==0:  # This will be True if there is an empty string
        messagebox.showinfo(title="Entry field error", message="Please enter a website")
    else:
        try:
            with open("Password_Manager/data.json", "r") as data_file: #Open file in read mode
                data = json.load(data_file) #Reading data from json file
        except FileNotFoundError:
            messagebox.showinfo(title="Data File Error", message="Data file does not exist yet.")
        else:   
            if website in data:
                email = data[website]["email:"]
                password = data[website]["password:"]
                print(email, password)
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Data Error", message=f"{website} does not exist in the database.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Password_Manager/logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Email/Username Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Website Entry
website_entry = Entry(width = 21)
website_entry.grid(column=1, row=1)
website_entry.focus()
# Email/Username Entry
email_username_entry = Entry(width = 35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "joesmith@gmail.com")
# Password Entry
password_entry = Entry(width = 21)
password_entry.grid(column=1, row=3)

# Setting up the Generate Password button
generate_password_button = Button(text = "Generate Password", command = generate_password)
generate_password_button.grid(column=2, row=3)
# Setting up the Add button
add_button = Button(text = "Add", width = 36, command = add)
add_button.grid(column=1, row=4, columnspan=2)
# Setting up the Search Website button
search_website_button = Button(text = "Search Website", width=13, command = find_password)
search_website_button.grid(column=2, row=1)
#Disable search button if nothing was entered into website field
# if len(website_entry.get()) == 0:
#     search_website_button.config(state=DISABLED)
# else:
#     search_website_button.config(state=NORMAL)

window.mainloop() #Keep the window open and forever looping though the program
