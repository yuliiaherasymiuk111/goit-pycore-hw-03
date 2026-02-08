from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_day = birthday_this_year

            if congratulation_day.weekday() == 5:
                congratulation_day += timedelta(days=2)
            elif congratulation_day.weekday() == 6:
                congratulation_day += timedelta(days=1)

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_day.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
