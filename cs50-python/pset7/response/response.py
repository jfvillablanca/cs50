import validators


def main():
    email = input("What's your email address? ")
    print(f"{'Valid' if validators.email(email) else 'Invalid'}")


if __name__ == "__main__":
    main()
