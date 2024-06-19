

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Are the recourses sufficient
def is_resources_sufficient(order_ingredients):
    """Returns true and order can be made, and false when resources are low"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not {item}.")
            is_enough = False
    return is_enough


# Create coins function for user to pay
def process_coins():
    """Returns the total calculated from all coins inserted into coffee machine"""
    print("Please insert coins.")
    total = int(input ("How many Quarters? ")) * 0.25
    total += int(input ("How many Dimes? ")) * 0.10
    total += int(input ("How many Nickels? ")) * 0.05
    total += int(input ("How many Pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns if money is enough to make coffe or refunds if money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money Refunded! ")
        return False

    # 7. Make the coffee function


def make_coffe(drink_name, order_ingredients):
    """ Returns the kind of drink to be made, and what ingredients to use, and deduct from supply"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    # 1. Prompt the user what kind of drink will the user like to make e.g. Latte/Expresso/Cappuccino
    choice = input("What would you like? (latte, espresso or cappuccino ")
    # 2. Turn off coffee machine by entering turn off  to the prompt
    if choice == "off":
        is_on = False
    # 3. Print and generate report of resources left
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"Money :{profit} ")
    # 4. Check if resources are sufficient
    else:
        drink = MENU[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            # 5. process the coins
            payment = process_coins()
            # 6. Check if transaction was successful
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])


