import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def is_resource_available():
    for item in menu[choice]["ingredients"]:
        if menu[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    global profit
    drink_cost = menu[choice]["cost"]
    print("Please insert coins")

    # Function to safely get coin input from the user
    def get_coin_input(coin_name):
        while True:
            try:
                value = int(input(f"How many {coin_name}?: "))
                if value < 0:
                    print("Please enter a positive number.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Get user input for each coin type
    quarters = get_coin_input("quarters")
    dimes = get_coin_input("dimes")
    nickels = get_coin_input("nickels")
    pennies = get_coin_input("pennies")

    total_money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    
    if total_money >= drink_cost:
        if total_money > drink_cost:
            print(f"Here's your change: ${total_money - drink_cost:.2f}")
            profit += drink_cost
            return True
        else:
            return True
    else:
        print(f"Sorry, that's not enough money. Please insert more coins.")
        return False

def make_coffee():
    global resources
    for item in menu[choice]["ingredients"]:
        resources[item] -= menu[choice]["ingredients"][item]
    print(f"Here is your ☕ {choice} ☕")
    

running = True

while running == True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    elif choice == "off":
        running = False
        break
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if is_resource_available() == True:
            if process_coins() == True:
                make_coffee()
            else:
                break
    else:
        print("Enter a valid drink!")
    input("Press enter to continue...")
    os.system("cls")
        
