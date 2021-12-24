import menu

running = True
money = 0


def calculate_if_enough(ingredientliste):
    if len(ingredientliste) == 2:
        if menu.resources["water"] > ingredientliste[0] and menu.resources["coffee"] > ingredientliste[1]:
            return True
        else:
            return False
    else:
        if menu.resources["water"] > ingredientliste[0] and menu.resources["coffee"] > ingredientliste[1] and \
                menu.resources["milk"] > ingredientliste[2]:
            return True
        else:
            return False


def insert_coins():
    quarter = input("quater:")
    dimes = input("dimes")
    nickel = input("nickel")
    pennies = input("pennies")
    return float(quarter)*0.25 + float(dimes)*0.1 + float(nickel)*0.05 + float(pennies)*0.01


while running == True:
    var = input("What would you like? (espresso/latte/cappuccino):")

    if var == "off":
        running = False
    elif var == "report":
        print(menu.resources)
    else:
        if var == "espresso" or var == "latte":
            too_less = calculate_if_enough(
                [menu.MENU[var]["ingredients"]["water"], menu.MENU[var]["ingredients"]["coffee"]])
        else:
            too_less = calculate_if_enough(
                [menu.MENU[var]["ingredients"]["water"], menu.MENU[var]["ingredients"]["coffee"],
                 menu.MENU[var]["ingredients"]["milk"]])
        if too_less == False:
            print("Sorry there is not enough water.")
        else:
            inserted_coins = insert_coins()
            print(f"{inserted_coins}")
