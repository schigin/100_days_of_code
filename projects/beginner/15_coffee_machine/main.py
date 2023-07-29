from coffee_machine_data import coffee_machine, drinks


def print_report(coffee_machine_data):
    """Prints current values of coffee machine resources."""
    print(f"Water: {coffee_machine_data['water']}ml")
    print(f"Milk: {coffee_machine_data['milk']}ml")
    print(f"Coffee: {coffee_machine_data['coffee']}g")
    print(f"Money: ${coffee_machine_data['money']}")


def get_drink_data(drinks_data, coffee):
    """Get data about chosen coffee drink."""
    return drinks_data[coffee]


def check_resources(coffee_machine_data, drink_data):
    """Checks if there are enough resources to make chosen drink."""
    if coffee_machine_data['water'] < drink_data['water']:
        print("Sorry there is not enough water.")
        return False
    elif coffee_machine_data['coffee'] < drink_data['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif coffee_machine_data['milk'] < drink_data['milk']:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def process_coins():
    """Asks to insert specific coins anc calculates total amount of money."""
    quarters = int(input("how many quarters ($0.25)?: "))
    dimes = int(input("how many dimes ($0.10)?: "))
    nickles = int(input("how many nickles ($0.05)?: "))
    pennies = int(input("how many pennies ($0.01)?: "))

    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def conduct_transaction(money, drink_data):
    """Checks if user has inserted enough money and gives a change."""
    change = round((money - drink_data['price']), 2)

    if change >= 0:
        print(f"Here is your ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def prepare_coffee(coffee_machine_data, drink_data):
    """Deducts resources from coffee machine to prepare coffee drink."""
    coffee_machine_data['water'] -= drink_data['water']
    coffee_machine_data['milk'] -= drink_data['milk']
    coffee_machine_data['coffee'] -= drink_data['coffee']
    coffee_machine_data['money'] += drink_data['price']
    return coffee_machine_data


switch_off = False

while not switch_off:
    answer = input("\tWhat would you like? (espresso/latte/cappuccino): ").lower()

    if answer == 'off':
        switch_off = True

    elif answer == 'report':
        print_report(coffee_machine)

    elif answer in drinks.keys():
        drink = get_drink_data(drinks, answer)
        is_enough_resources = check_resources(coffee_machine, drink)

        if is_enough_resources:
            print(f"Price for {answer} is ${drink['price']}. Please insert coins.")
            inserted_money = process_coins()

            is_transaction_successful = conduct_transaction(inserted_money, drink)
            if is_transaction_successful:
                coffee_machine = prepare_coffee(coffee_machine, drink)
                print(f"Here is your {answer} ☕️. Enjoy!")