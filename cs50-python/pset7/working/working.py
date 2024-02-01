import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"(\d+)(?::?(\d+)?) ((?:A|P)M) to (\d+)(?::?(\d+)?) ((?:A|P)M)", s
    ):
        time_in_hours = convert_hour(matches.group(1), matches.group(3))
        time_in_minutes = convert_minutes(matches.group(2))
        time_out_hours = convert_hour(matches.group(4), matches.group(6))
        time_out_minutes = convert_minutes(matches.group(5))

        if (
            not 0 <= time_in_hours < 24
            or not 0 <= time_out_hours < 24
            or not 0 <= time_in_minutes <= 59
            or not 0 <= time_out_minutes <= 59
        ):
            raise ValueError

        return f"{time_in_hours:02}:{time_in_minutes:02} to {time_out_hours:02}:{time_out_minutes:02}"
    raise ValueError


def convert_hour(hour, meridiem):
    if meridiem == "AM" and hour == "12":
        return 0
    if meridiem == "PM" and hour != "12":
        return int(hour) + 12
    return int(hour)


def convert_minutes(minute):
    if minute:
        return int(minute)
    return 0


if __name__ == "__main__":
    main()
