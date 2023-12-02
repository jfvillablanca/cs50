greeting = input("Greeting: ").strip().lower()
if greeting[0 : len("hello")] == "hello":
    print("$0")
elif greeting[0:1] == "h":
    print("$20")
else:
    print("$100")
