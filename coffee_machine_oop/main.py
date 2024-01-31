from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    drink_options = menu.get_items()
    selection = input(f"What would you like to drink? ({drink_options}): ")
    if selection == "off":
        is_on = False    
    elif selection == "report":
        money_machine.report()
        coffee_maker.report()  
    else:
        drink = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)