import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    for i, csv_file in enumerate(sys.argv[1:]):
        if csv_file[-4:] != ".csv":
            sys.exit(f"File {i + 1} is not a CSV file")

    students = []
    try:
        with open(sys.argv[1], encoding="utf-8") as read_csv:
            reader = csv.DictReader(read_csv)
            for row in reader:
                last_name, first_name = row["name"].split(",")
                students.append(
                    {
                        "first": first_name.strip(),
                        "last": last_name,
                        "house": row["house"],
                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    try:
        with open(sys.argv[2], "w", encoding="utf-8") as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=students[0].keys())
            writer.writeheader()
            for student in students:
                writer.writerow(student)
    except FileNotFoundError:
        sys.exit(f"Could not write {sys.argv[2]}")


if __name__ == "__main__":
    main()
