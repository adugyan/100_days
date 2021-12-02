def main():
    powered_on: bool = True
    water, milk, coffee, money = set_resources(300, 200, 100, 0)
    while powered_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'report':
            print(f"""
            Water: {water}ml
            Milk: {milk}ml
            Coffee: {coffee}g
            Money: ${money}
            """)
            main()
        elif user_input == 'off':
            powered_on = False
        elif user_input == 'latte':
            new_w, new_milk, new_c, new_m = create_latte(water, milk, coffee, money)
            water, milk, coffee, money = set_resources(new_w, new_milk, new_c, new_m)


def set_resources(new_w, new_milk, new_c, new_m) -> (int, int, int, float):
    """
    Will return the amount of resources left for Water, Milk, Coffee, and Money.
    :return:
    """
    water: int = new_w
    milk: int = new_m
    coffee: int = new_c
    money: float = new_m
    return water, milk, coffee, money


def get_resources() -> (int, int, int, float):
    water, milk, coffee, money = set_resources()
    return water, milk, coffee, money


def receive_coins() -> (float, float):
    total_quarters: float = 0
    total_dimes: float = 0
    total_nickels: float = 0
    total_pennies: float = 0

    print("Please insert coins")
    total_quarters = float(input("How many quarters?: "))
    total_dimes = float(input("How many dimes?: "))
    total_nickels = float(input("How many nickels?: "))
    total_pennies = float(input("How many pennies?: "))

    return total_quarters, total_dimes, total_nickels, total_pennies


def calculate_cash() -> float:
    """
    This function will take the coins given in receive_coins and return the total amount the user has
    put into the machine
    :return:
    """
    quarters: float = 0.25
    dimes: float = 0.10
    nickels: float = 0.05
    pennies: float = 0.01
    money_put_in: float
    quarters_received, dimes_received, nickels_received, pennies_received = receive_coins()

    quarters = quarters_received * quarters
    dimes = dimes_received * dimes
    nickels = nickels_received * nickels
    pennies = pennies_received * pennies

    money_put_in = quarters + dimes + nickels + pennies
    return money_put_in


def create_latte(water, milk, coffee, money):
    """
    Ensures that the user has entered enough money to buy the latte. Ensures there are enough resources. If there are
    complete the transaction and return how many resources are still left.
    :return:
    """
    print("That'll be $2.50 ")
    cash_amount = calculate_cash()

    if water >= 200 and milk >= 150 and coffee >= 24:
        water = water - 200
        milk = milk - 150
        coffee = coffee - 24
    else:
        print("Sorry. There are insufficient ingredients to complete your request.")

    if cash_amount >= 2.50:
        money = money + 2.50
        print("Here is your latte ☕. Enjoy!")
        change = cash_amount - 2.50
        print(f"Here's your change: {change}")

    return water, milk, coffee, money

main()
