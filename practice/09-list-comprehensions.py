# https://www.hackerrank.com/challenges/list-comprehensions/problem


def create_list(x, y, z, n):
    i = range(x + 1)
    j = range(y + 1)
    k = range(z + 1)

    result = [[a, b, c] for a in i for b in j for c in k if a + b + c != n]
    print(result)


if __name__ == "__main__":
    x = int(input())  # "x: "
    y = int(input())  # "y: "
    z = int(input())  # "z: "
    n = int(input())  # "n: "

    create_list(x, y, z, n)
