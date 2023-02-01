from menu import MENU, resources


def main():
    off = False
    while not off:
        # Check that the user entered the correct input
        while True:
            response = input("What would you like? \
                (espresso/latte/cappuccino): ")
            if response in [
                "espresso",
                "latte",
                "cappuccino",
                "off",
                "report"
            ]:
                break
            else:
                print("Invalid input")

        # Program exits if user enteres "off"
        if response == "off":
            off = True

        # What to do if the user whats coffee
        else:
            # Print a report of the current resources
            if response == "report":
                print_resources()

            # Make some coffee
            elif response == "espresso":
                make_coffee("espresso")

            elif response == "latte":
                make_coffee("latte")

            elif response == "cappuccino":
                make_coffee("cappuccino")


def check_resources(drink):
    ingredient_list = MENU[drink]["ingredients"]
    for ingredient in ingredient_list:
        if resources[ingredient] < ingredient_list[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def insert_coins():
    coins = {
        "quarters": {"num": 0, "value": 0},
        "dimes": {"num": 0, "value": 0},
        "nickles": {"num": 0, "value": 0},
        "pennies": {"num": 0, "value": 0},
        }
    for coin in coins:
        coins[coin]["num"] = int(input(f"How many {coin}?: "))
    coins["quarters"]["value"] = coins["quarters"]["num"] * 0.25
    coins["dimes"]["value"] = coins["dimes"]["num"] * 0.10
    coins["nickles"]["value"] = coins["nickles"]["num"] * 0.05
    coins["pennies"]["value"] = coins["pennies"]["num"] * 0.01
    return coins


def calculate_total(coins):
    total = 0
    for coin in coins:
        total += coins[coin]["value"]
    print(f"You entered ${total}")
    return total


def check_money(drink, x):
    if MENU[drink]["cost"] <= x:
        print("You inserted enough money")
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def calculate_change(drink, x):
    change = round(x - MENU[drink]["cost"], 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")


def update_resources(drink):
    ingredient_list = MENU[drink]["ingredients"]
    for ingredient in ingredient_list:
        resources[ingredient] -= ingredient_list[ingredient]
    resources["money"] += MENU[drink]["cost"]


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def make_coffee(drink):
    # Check if there are enough resources to make a espresso
    if check_resources(drink):
        print(f"The cost of an {drink} is ${MENU[drink]['cost']}")
        coins = insert_coins()
        total_of_coins_inserted = calculate_total(coins)
        if check_money(drink, total_of_coins_inserted):
            calculate_change(drink, total_of_coins_inserted)
            update_resources(drink)
            print(f"Here is your {drink}. Enjoy")
        else:
            off = True
    else:
        off = True


main()
