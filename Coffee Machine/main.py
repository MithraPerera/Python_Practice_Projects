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


# PROCEDURAL VERSION OF THE CODE BELOW

# from art import logo
#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def collect_coins(type_coffee):
#     """Processes the coins and returns True if the payment is enough for the drinks cost and False otherwise."""
#     print("Please insert coins.")
#     quarters = int(input("How many quarters?: "))
#     dimes = int(input("How many dimes?: "))
#     nickles = int(input("How many nickles?: "))
#     pennies = int(input("How many pennies?: "))
#     total_inputted = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
#     cost = MENU[type_coffee]["cost"]
#
#     if total_inputted >= cost:
#         change = total_inputted - cost
#         print("💵: Here is ${:.2f} in change.".format(change))
#         print(f"☕️: Here is your {type_coffee}. Enjoy!")
#         return True
#     else:
#         print("Sorry that is not enough money. Money refunded.")
#         return False
#
#
# def check_ingredients(type_coffee):
#     """Returns True if there is enough resources to make the drink and False otherwise with a message of what is lacking."""
#     if (MENU[type_coffee]["ingredients"]["water"] <= resources["water"]) and (
#             MENU[type_coffee]["ingredients"]["milk"] <= resources["milk"]) and (
#             MENU[type_coffee]["ingredients"]["coffee"] <= resources["coffee"]):
#         return True
#     else:
#         if MENU[type_coffee]["ingredients"]["water"] > resources["water"]:
#             print("Sorry, there is not enough water.")
#         if MENU[type_coffee]["ingredients"]["milk"] > resources["milk"]:
#             print("Sorry, there is not enough milk.")
#         if MENU[type_coffee]["ingredients"]["coffee"] > resources["coffee"]:
#             print("Sorry, there is not enough coffee.")
#         return False
#
#
# def use_resources(type_coffee):
#     """Subtracts used resources based on the drink that is made."""
#     # resources["water"] -= MENU[type_coffee]["ingredients"]["water"]
#     # resources["milk"] -= MENU[type_coffee]["ingredients"]["milk"]
#     # resources["coffee"] -= MENU[type_coffee]["ingredients"]["coffee"]
#     for item in MENU[type_coffee]["ingredients"]:
#         resources[item] -= MENU[type_coffee]["ingredients"][item]
#
#
# def coffee_machine():
#     """Infinitely loops through the coffee machine program."""
#     profit = 0.00
#     while True:
#         type = input("What would you like? ('e' - espresso/'l' - latte/'c' - cappuccino): ")
#         if type == "off":
#             break
#         elif type == "report":
#             print(f"Water: {resources['water']}")
#             print(f"Milk: {resources['milk']}")
#             print(f"Coffee: {resources['coffee']}")
#             print("Profit: {:.2f}".format(profit))
#         else:
#             enough_ingredients = check_ingredients(type)
#             if enough_ingredients:
#                 successful_purchase = collect_coins(type)
#                 if successful_purchase:
#                     profit += MENU[type]["cost"]
#                     use_resources(type)
#
#
# print(logo)
# print("PRICES: Espresso = $1.50, Latte = $2.50, Cappuccino = $3.00")
# coffee_machine()