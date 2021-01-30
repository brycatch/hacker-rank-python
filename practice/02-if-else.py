# https://www.hackerrank.com/challenges/py-if-else/problem


def if_else(n):
    first_range = range(2, 6)
    second_range = range(6, 21)

    if bool(n % 2):
        print("Weird")
    else:
        if n in first_range:
            print("Not Weird")
        elif n in second_range:
            print("Weird")
        else:
            print("Not Weird")


if __name__ == "__main__":
    n = int(input().strip())
    if_else(n)