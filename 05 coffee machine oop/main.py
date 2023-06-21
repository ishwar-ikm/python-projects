from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()
make = CoffeeMaker()
money = MoneyMachine()

while True:
    order = input("What would you like to have? " + item.get_items() + ": ")
    if order == "report":
        make.report()
        money.report()
    elif order == "off":
        break
    else:
        drink = item.find_drink(order)
        if make.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                make.make_coffee(drink)