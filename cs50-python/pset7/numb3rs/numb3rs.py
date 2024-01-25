import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(
        r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",
        ip,
    ):
        for i in range(1, 5):
            octet = int(matches.group(i))
            print(octet)
            if not 0 <= octet <= 255:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()
