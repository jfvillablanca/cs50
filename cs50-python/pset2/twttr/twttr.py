voweled_string = input("Input: ")
devoweled_string = ""
for char in voweled_string:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
        devoweled_string += char
print(f"Output: {devoweled_string}")
