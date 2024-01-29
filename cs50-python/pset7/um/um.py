import re


def main():
    print(count(input("Text: ")))


def count(s):
    words = re.split(r"(\w+)", s)
    return len([word for word in words if word.lower() == "um"])


if __name__ == "__main__":
    main()
