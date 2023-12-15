import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")

    linecount = 0
    try:
        with open(sys.argv[1], encoding="utf-8") as file:
            for line in file:
                if line.strip() == "" or line.lstrip().startswith("#"):
                    continue
                linecount += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(linecount)


if __name__ == "__main__":
    main()
