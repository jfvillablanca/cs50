COKE_PRICE = 50
amount_due = COKE_PRICE

while True:
    coin = int(input("Insert Coin: "))
    match coin:
        case 25:
            amount_due -= 25
        case 10:
            amount_due -= 10
        case 5:
            amount_due -= 5
    if amount_due <= 0:
        break
    print(f"Amount Due: {amount_due}")
print(f"Change Owed: {-amount_due}")

