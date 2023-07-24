# Define the menu of available beverages with their ingredients and cost
menu = {
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

# Define the available amount of ingredients and profit of the machine
amount = {
    'water': 800,
    'milk': 550,
    'coffee': 400,
    'profit': 0,
}

# Function to display the current status of resources and profit
def report():
    print(f"Water: {amount['water']}ml")
    print(f"Milk: {amount['milk']}ml")
    print(f"Coffee: {amount['coffee']}g")
    print(f"Profit: ${amount['profit']}")

# Function to receive payment and return the total amount
def payment():
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    return quarters + dimes + nickels + pennies

# Function to check if the payment is sufficient for the selected beverage
def is_sufficient_amount(payment_amount, order):
    if payment_amount >= menu[order]['cost']:
        return True
    else:
        return False

# Function to update the resources and profit after successful transaction
def make_transaction(payment_amount, order):
    amount['profit'] += menu[order]['cost']
    for item in menu[order]['ingredients']:
        amount[item] -= menu[order]['ingredients'][item]
    return payment_amount - menu[order]['cost']

# Function to check if there are enough resources to make the selected beverage
def is_enough_resources(order):
    ingredients = menu[order]['ingredients']
    for item in ingredients:
        if ingredients[item] > amount[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# Function to control the coffee machine and handle user choices
def machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "report" or choice == "off":
            break
        print("Enter a valid input!")

    if choice == "off":
        return "off"

    if choice == "report":
        report()

    else:
        if is_enough_resources(choice):
            payment_amount = payment()
            if is_sufficient_amount(payment_amount, choice):
                print(f"Your change: ${round(make_transaction(payment_amount, choice), 2)}")
                print(f"Here is your {choice}. Enjoy!")

            else:
                print("Sorry not enough balance added! Refunding amount...")


# Main loop to keep the coffee machine running
while True:
    choice = machine()
    if choice == "off":
        print("Machine shutting off...")
        break
