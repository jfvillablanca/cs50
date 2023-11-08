import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py database.csv sequence.txt")

    people = []
    with open(sys.argv[1], encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for person in reader:
            people.append(
                {
                    key: int(value) if key != "name" else value
                    for key, value in person.items()
                }
            )

    with open(sys.argv[2], encoding="utf-8") as file:
        sequence = file.readline()

    # Create a dict based on the STRs in the database's header
    strs = [x for x in people[0].keys() if x != "name"]
    longest_strs = {s: longest_match(sequence, s) for s in strs}

    # Iterate on all people to be matched and check if all
    # STRs satisfy the longest str condition
    for person in people:
        is_match = True
        for s in strs:
            if person[s] != longest_strs[s]:
                is_match = False

        if is_match:
            print(person["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
