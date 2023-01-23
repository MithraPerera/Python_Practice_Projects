from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(logo)
print("PRICES: Espresso = $1.50, Latte = $2.50, Cappuccino = $3.00")

while True:
    type_coffee = input(f"What would you like?({menu.get_items()}): ")

    if type_coffee == "off":
        break
    elif type_coffee == "report":
        coffee_maker.report()
        money_machine.report()

    drink = menu.find_drink(type_coffee)
    if drink is not None:
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            successful_payment = money_machine.make_payment(drink.cost)
            if successful_payment:
                coffee_maker.make_coffee(drink)