def main():
    time = input("What time is it? ").split()
    if len(time) != 1:
        time[0] = change_format_to_24_hour(time)

    converted_time = convert(time[0])
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = map(float, time.split(":"))
    return hour + (minute / 60)


def change_format_to_24_hour(time_12):
    meridian = time_12[1].lower()
    hour, minute = time_12[0].split(":")

    if meridian == "am":
        if hour == "12":
            return f"0:{minute}"
        return f"{hour}:{minute}"

    return f"{int(hour) + 12}:{minute}"


if __name__ == "__main__":
    main()
