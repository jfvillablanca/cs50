def main():
    greeting = input("Greeting: ").strip().lower()
    print(value(greeting))


def value(greeting):
    if greeting.lower()[0 : len("hello")] == "hello":
        return 0
    if greeting.lower()[0:1] == "h":
        return 20
    return 100


if __name__ == "__main__":
    main()
