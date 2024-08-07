from os import system, name

import menu


def process_coins():
    """Returns the total calculated from coins inserted by user."""
    print("Please insert coins.")
    total = 0
    try:
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return process_coins()
    return total


def print_report(resources, profit):
    """
    Print a report of resources available in the coffee_machine.
    """
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    funds_in_machine = round(profit, 2)

    print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${funds_in_machine}")


def check_resources(type_of_coffee, resources):
    """
    Check if coffee machine has enough resources to create the type of coffee.
    :param type_of_coffee: user choice (espresso, latte, cappuccino).
    :param resources: available resources in the coffee machine
    :return: Boolean, True if there are enough resources, False otherwise
    """
    for item in type_of_coffee['ingredients']:
        if type_of_coffee['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost, profit):
    """
    Check if enough money is received for the choice of drink
    If too much money is received the excess is refunded
    If not enough money is received, all of it is refunded to the user
    :return: Boolean, True if tx successful, otherwise False
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        profit += drink_cost
        return True, profit
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, profit


def make_coffee(type_of_coffee):
    """
    Make the coffee and reduce the ingredients from the resources.
    """
    print(f"Here is your {type_of_coffee} ☕️!")


def reduce_resources(drink, resources):
    """Reduce ingredients in coffee machine resources"""
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]


def get_user_input():
    """
    Get user input, (espresso, latte, cappuccino, report, off)
    :return: User choice
    """
    while True:
        choice = str(input("What would you like? (espresso/latte/cappuccino): ")).casefold()
        if choice in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
            return choice
        else:
            print("Please enter a valid option")


def clear_console():
    """Clears the console screen"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def coffee_machine():
    """Main coffee_machine function."""
    profit = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    coffee_machine_on = True

    while coffee_machine_on:
        choice = get_user_input()
        # check if coffee machine is to be turned OFF need to print a report
        if choice == 'off':
            coffee_machine_on = False
            clear_console()
        elif choice == 'report':
            print_report(resources, profit)
        else:
            drink = menu.MENU[choice]
            if check_resources(drink, resources):
                payment = process_coins()
                transaction_successful, profit = is_transaction_successful(payment, drink['cost'], profit)
                if transaction_successful:
                    reduce_resources(drink, resources)
                    make_coffee(choice)


if __name__ == "__main__":
    coffee_machine()
