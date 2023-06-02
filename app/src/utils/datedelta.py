from datetime import timedelta, date

def days_until_next(date_of_birth) -> timedelta:
    # Get today's date
    today = date.today()

    # Replace the year of the given date with the current year
    date_of_birth = date_of_birth.replace(year=today.year)

    # If the birthdate has already occurred this year, set it for next year
    if date_of_birth < today:
        date_of_birth = date_of_birth.replace(year=today.year + 1)

    # Calculate the difference between the birthdate and today's date
    delta = date_of_birth - today

    # Return the timedelta object representing the difference in days
    return delta
