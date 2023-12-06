def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    num, den = fraction.split("/")
    if not num.isdigit() or not den.isdigit():
        raise ValueError
    num, den = map(float, [num, den])
    if den == 0:
        raise ZeroDivisionError
    if num > den:
        raise ValueError
    return round(num * 100 / den)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
