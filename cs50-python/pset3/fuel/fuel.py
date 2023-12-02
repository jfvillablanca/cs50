while True:
    try:
        fraction = input("Fraction: ")
        num, den = fraction.split("/")
        if not num.isdigit() or not den.isdigit():
            raise ValueError
        num, den = map(float, [num, den])
        if num > den:
            raise ValueError
        fuel = round(num * 100 / den)
        break
    except (ValueError, ZeroDivisionError):
        pass
if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel}%")
