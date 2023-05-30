from datetime import timedelta, date


def days_until_next(date_of_birth) -> timedelta:
    today = date.today()
    date_of_birth = date_of_birth.replace(year=today.year)

    if date_of_birth < today:
        date_of_birth = date_of_birth.replace(year=today.year + 1)

    return date_of_birth - today
