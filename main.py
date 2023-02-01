from menu import MENU, resources

off = False

def check_resources(drink):
    ingredient_list = MENU[drink]["ingredients"]
    for ingredient in ingredient_list:
        # print(f"{resources[ingredient}")
        if resources[ingredient] < ingredient_list[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        else:
            return True

def insert_coins():
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
        }
    for coin in coins:
        coins[coin] = input(f"How many {coin}?: ")   
    return coins

while not off:
    while True:
        response = input("What would you like? (espresso/latte/cappuccino): ")
        if response in ["espresso", "latte", "cappuccino", "off", "report"]:
            break
        else:
            print("Invalid input")

    if response == "off":
        off = True

    else:
        if response == "report":
            for resource in resources:
                print(f"{resource.title()}: ${resources[resource]} ")
        elif response == "espresso":
            # Check if there are enough resources to make a espresso
            if not check_resources("espresso"):
                off = True
            else:
                coins = insert_coins()
                print("You entered")
                for coin in coins:
                    print(f"{coins[coin]} {coin}")

        elif response == "latte":
            # Check if there are enough resources to make a espresso
            if not check_resources("latte"):
                off = True
            else:
                print("We're good to go!")
        elif response == "cappuccino":
            # Check if there are enough resources to make a espresso
            if not check_resources("cappuccino"):
                off = True
            else:
                print("We're good to go!")


