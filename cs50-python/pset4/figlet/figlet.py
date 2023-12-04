import sys
from random import choice

from pyfiglet import Figlet


def main():
    figlet = Figlet()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Invalid usage")
        sys.exit(1)
    if len(sys.argv) == 3:
        is_invalid_font_flag = sys.argv[1] != "-f" and sys.argv[1] != "--font"
        is_invalid_font_name = sys.argv[2] not in figlet.getFonts()
        if is_invalid_font_flag or is_invalid_font_name:
            print("Invalid usage")
            sys.exit(1)

    font = get_font_choice(figlet)
    my_string = input("Input: ")
    figlet.setFont(font=font)

    print(figlet.renderText(my_string))


def get_font_choice(figlet):
    if len(sys.argv) == 3:
        return sys.argv[2]
    return choice(figlet.getFonts())


if __name__ == "__main__":
    main()
