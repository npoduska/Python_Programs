MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Add up the total amount of money put into the machine.
def money_function():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

#Money calculation function
def enough_money(total_money_input, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if total_money_input >= cost:
        change = round(total_money_input - drink_cost, 2)
        print(f"Your change is: ${change}.")
        global total_money
        total_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def enough_resoures(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(drink_selection, drink_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_selection} ☕️. Enjoy!")
            
##Machine Operations
#Choose a drink
#Show how much it costs, accepting only coins
#Also show if there is enough water, milk, or coffee available to make the drink. If not, user needs to pick another drink.
#User needs to insert coins if conditions are right.
#Give a thank you and preparing drink message.
#Show how much change is given. Update amount of money in machine.
#Thank you message after drink is made. Update resource amounts in machine.

# Initial Settings
total_money = 0
machine_on = True

while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino):")
    total_money_input = 0
    if selection == "espresso" or selection == "e":
        selection = "espresso"
        items = MENU["espresso"]
        if enough_resoures(items["ingredients"]):
            cost = items["cost"]
            print(f"That will be ${cost}0.")
            confirm = input("Type 'y' or 'n' to confirm this is what you'd like.")
            if confirm == "y":
                payment = money_function()
                if enough_money(payment, items["cost"]):
                    make_coffee(selection, items["ingredients"])
                    
    elif selection == "latte" or selection == "l":
        selection = "latte"
        items = MENU.get("latte")
        if enough_resoures(items["ingredients"]):
            cost = items["cost"]
            print(f"That will be ${cost}0.")
            confirm = input("Type 'y' or 'n' to confirm this is what you'd like.")
            if confirm == "y":
                payment = money_function()
                if enough_money(payment, items["cost"]):
                    make_coffee(selection, items["ingredients"])
                    
    elif selection == "cappuccino" or selection == "c":
        selection = "cappuccino"
        items = MENU.get("cappuccino")
        if enough_resoures(items["ingredients"]):
            cost = items["cost"]
            print(f"That will be ${cost}0.")
            confirm = input("Type 'y' or 'n' to confirm this is what you'd like.")
            if confirm == "y":
                payment = money_function()
                if enough_money(payment, items["cost"]):
                    make_coffee(selection, items["ingredients"])
                    
    elif selection == "report" or selection == "r":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total_money}")
        
    elif selection == "off":
        machine_on = False
        
        
        
        