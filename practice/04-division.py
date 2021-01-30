# https://www.hackerrank.com/challenges/python-division/problem


def integer_division(a, b):
    print(a // b)


def float_division(a, b):
    print(a / b)


if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())

    integer_division(a, b)
    float_division(a, b)