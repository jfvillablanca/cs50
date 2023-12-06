def main():
    voweled_string = input("Input: ")
    print(f"Output: {shorten(voweled_string)}")


def shorten(word):
    devoweled_word = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            devoweled_word += char
    return devoweled_word


if __name__ == "__main__":
    main()
