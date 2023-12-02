from datetime import datetime

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ")
        if date.count("/") == 2:
            month, day, year = map(int, date.split("/"))
            if month < 1 or month > 12:
                raise ValueError
        else:
            month_name, day, year = date.split()
            if month_name.title() not in months or "," not in day:
                raise ValueError

            month = months.index(month_name) + 1
            day, year = map(int, [day.removesuffix(","), year])

        if day < 1 or day > 31:
            raise ValueError
        break
    except ValueError:
        pass

d = datetime(year, month, day)
print(f"{d:%Y-%m-%d}")
