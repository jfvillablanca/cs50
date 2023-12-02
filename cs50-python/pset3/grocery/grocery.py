groceries = {}

while True:
    try:
        item = input().strip()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        break

for item in sorted(groceries):
    print(f"{groceries[item]} {item.upper()}")
