from concurrent.futures import process


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

is_on = True
profit = 0

def is_resource_sufficient(ordered_ingredient):
    """check is resources is sufficient

    Args:
        ordered_ingredient ([type]): [description]

    Returns:
        [type]: [bool]
    """
    for item in ordered_ingredient:
        if ordered_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    """total caluculated from coins inserted by user

    Returns:
        [type]: [float]
    """
    print("Please insert coins: ")
    total = int(input("how many quarters ? : "))*0.25
    total += int(input("how many dimes ? : "))*0.1
    total += int(input("how many nickles ? : "))*0.05
    total += int(input("how many pennies ? : "))*0.01
    return total
def is_payment_successful(money_given,cost):
    """return true when payment is successful else false
    Args:        
        cost ([type]): [bool]
    """
    if money_given >= cost:
        global profit 
        profit += cost
        change = round(money_given - cost,2)
        print(f"Here is your coffee ☕  and {change} refund. Enjoy !")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def remaining_resources(order):
    for item in order:
        resources[item] -= order[item]
    
def resource_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

        


while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        resource_report()
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):            
            payment = process_coins()
            if is_payment_successful(payment,drink['cost']):
                remaining_resources(drink["ingredients"])
