import random


def main():
    score = 0
    level = get_level()
    problems = [generate_integer(level) for _ in range(10)]

    for problem in problems:
        tries = 0
        while True:
            print(f"{problem[0]} + {problem[1]} = ", end="")
            try:
                answer = int(input())
                if problem[0] + problem[1] != answer:
                    raise ValueError
                score += 1
                break
            except ValueError:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{problem[0]} + {problem[1]} = {problem[0] + problem[1]}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)


if __name__ == "__main__":
    main()
