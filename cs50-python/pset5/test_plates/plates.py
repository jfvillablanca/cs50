def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if any(not char.isalnum() for char in s):
        return False
    split = s.split("0")
    if len(split) != 1:
        # check if the number section starts with zero
        # e.g. s = 'abc01'; s.split("0")[0] should have
        # digits but it does not thus an invalid license plate
        if split[0].isalpha():
            return False
        # check if the rest of the number section does not
        # contain non-digit chars
        if len(split[1]) != 0 and not split[1].isdigit():
            return False
    return True


if __name__ == "__main__":
    main()
