from cs50 import get_float


def main():
    while True:
        cents = get_float("Change owed: ")
        if cents > 0:
            break

    cents = int(cents * 100)

    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    pennies = calculate_pennies(cents)
    print("{}".format(quarters + dimes + nickels + pennies))


def calculate_quarters(cents):
    return int(cents / 25)


def calculate_dimes(cents):
    return int(cents / 10)


def calculate_nickels(cents):
    return int(cents / 5)


def calculate_pennies(cents):
    return int(cents)


if __name__ == "__main__":
    main()
