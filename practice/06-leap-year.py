# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap_year(year):
    year_is_valid = 1900 <= year and year <= 10 ** 5

    # If year % {number} is 0, the year is divisible by the {number}
    year_divided_by_4 = not bool(year % 4)
    year_divided_by_100 = not bool(year % 100)
    year_divided_by_400 = not bool(year % 400)

    return year_is_valid and (
        (year_divided_by_4 and not year_divided_by_100) or year_divided_by_400
    )


if __name__ == "__main__":
    year = int(input().strip())
    print(is_leap_year(year))