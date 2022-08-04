from replit import clear

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

# TODO 1 Turn on machine
sta = False
game = True
resources["money"] = 0


def turn_on(sta):
    sta = True
    return sta


def turn_off(sta):
    sta = False
    return sta


# TODO 2 PRINT REPORT
def print_resources(resources):
    return resources


# TODO 3 check if resources are enough
def check_resources(choice, resources, game):
    if choice == "espresso":
        if MENU[choice]["ingredients"]["water"] > resources["water"]:
            print("You need more water to make an expresso")
        elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            print("You need more coffee to make an espresso")
        else:
            # collect monney
            check_money(choice, resources, game)
    elif choice == "latte" or choice == "cappuccino":
        if MENU[choice]["ingredients"]["water"] > resources["water"]:
            print(f"You need more water to make a {choice}")
        elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            print(f"You need more coffee to make a {choice}")
        elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
            print("You need more milk to make a {choice}")
        else:
            # collect money
            check_money(choice, resources, game)


# check money
def check_money(choice, resources, game):
    penny = float(input("How many pennies?"))
    nickle = float(input("How many nickles?"))
    dime = float(input("How many dimes?"))
    quarter = float(input("How many quarters?"))

    penny *= 0.01
    nickle *= 0.05
    dime *= 0.10
    quarter *= 0.25
    total = penny + nickle + dime + quarter

    # get the price of the choice
    cost = MENU[choice]["cost"]
    print(f"penny: {penny}, total: {total}, cost: {choice} is {cost} ")
    # check if the money is not enough
    if total < cost:
        print(f"You do not have sufficient amount to make a {choice}")
        # ask to turn off or restart
        game = False
    else:
        # subtract the resources
        if choice == "espresso":
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]

            # add money to the coffe machine
            resources["money"] += MENU[choice]["cost"]

            # give change
            balance = round(total - MENU[choice]["cost"])
            print(f"Your balance is {balance} \n Your resources remaining are: {resources}")
            print(f'Enjoy your delicious cup of {choice}')

            # ask to restart
            restart = input("Would you like another drink? y or no \n")
            if restart == "y":
                clear()
                start_game(resources, game)
            game = False
        elif choice == "latte" or choice == "cappuccino":
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]

            # add money to the coffe machine
            resources["money"] += MENU[choice]["cost"]

            # give change
            balance = total - MENU[choice]["cost"]
            print(f"Your balance is {balance} \n Your resources remaining are: {resources}")
            print(f'Enjoy your delicious cup of {choice}')
            # ask to restart
            restart = input("Would you like another drink? y or no \n")
            if restart == "y":
                clear()
                start_game(resources, game)
            game = False


def start_game(resources, game):
    # check available resources
    report = input("would you like to see your resources? y or n \n").lower()
    if report == "y":
        print(resources)
    # Prompt User
    choice = input("What would you like? espresso/latte/cappuccino").lower()
    # check if the resources is available
    check_resources(choice, resources, game)


start_game(resources, game)  