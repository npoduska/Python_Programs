alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #Check if the character is in the alphabet.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

#Import and print the logo from art.py when the program starts.
from caesar_cipher_art import logo
print(logo)

#Continue using the program?
should_continue = True
while should_continue:
    #The inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #Make sure the shift amount is within the alphabet's range.
    shift = shift % 26
    
    #Calling the caesar module.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    #Does user want to continue?
    result = input("Type 'yes' if you want to go again. Else, type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")