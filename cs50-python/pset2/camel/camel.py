camel_string = input("camelCase: ")
snake_string = ""
for char in camel_string:
    if char.isupper():
        snake_string += f"_{char.lower()}"
    else:
        snake_string += char

print(f"snake_case: {snake_string}")
