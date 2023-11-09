import re

from cs50 import get_string


def main():
    cc = get_string("Number: ")
    if luhn(int(cc)):
        if check_string("34|37", 15 - 2, cc):
            print("AMEX")
            return
        if check_string("51|52|53|54|55", 16 - 2, cc):
            print("MASTERCARD")
            return
        if check_string("4", 16 - 1, cc) or check_string("4", 13 - 1, cc):
            print("VISA")
            return
    print("INVALID")


def luhn(cc_number):
    cumsum_one = 0
    cumsum_two = 0

    while cc_number > 0:
        cumsum_two += cc_number % 10
        cc_number = int(cc_number / 10)
        alternating_sum = 2 * (cc_number % 10)
        if alternating_sum >= 10:
            cumsum_one += alternating_sum % 10
            alternating_sum = int(alternating_sum / 10)
        cumsum_one += alternating_sum
        cc_number = int(cc_number / 10)

    return (cumsum_one + cumsum_two) % 10 == 0


def check_string(leading_digits, length, cc_string):
    pattern = r"^({})\d{{{}}}$".format(leading_digits, length)

    regex = re.compile(pattern)

    if regex.match(cc_string):
        return True
    return False


if __name__ == "__main__":
    main()
