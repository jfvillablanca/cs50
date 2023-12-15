import csv
import sys

from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, tablefmt="grid", headers="keys"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
