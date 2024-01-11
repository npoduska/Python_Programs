print("Welcome to the Tip Calculator.")

# Inputs, make sure they are numbers and not strings
bill=float(input("What was the total bill?"))
people=int(input("How many people will split the bill?"))
tip=(int(input("What percentage tip would you like to give? 10, 12, or 15%?")))

# Calculate the total bill with tip
tip_with_bill=tip/100*bill+bill
# Calculate the tip per person
tip_per_person=(tip/100*bill/people)

# Calculate the total each person needs to pay, with tip included
total=(tip_with_bill/people)

#Format tip and the final bill and print it out
tip_per_person="{:.2f}".format(tip_per_person)
total="{:.2f}".format(total)
print(f"Tip per person: ${tip_per_person}")
print(f"Each person should pay: ${total}")