def is_leap_year(year):
    return (is_divisible(year, 4) and not is_divisible(year, 100)) or is_divisible(year, 400)


def is_valid_month(month):
    return 1 <= month <= 12


def has_30_days(month):
    return month == 4 or month == 6 or month == 9 or month == 11


def has_31_days(month):
    return month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12


def has_28_days(month, year):
    return not is_leap_year(year) and month == 2


def has_29_days(month, year):
    return is_leap_year(year) and month == 2


def is_valid_date(day, month, year):
    return is_valid_month(month) and (
        (has_31_days(month) and 1 <= day <= 31) or
        (has_30_days(month) and 1 <= day <= 30) or
        (has_29_days(month, year) and 1 <= day <= 29) or
        (has_28_days(month, year) and 1 <= day <= 28)
    )
