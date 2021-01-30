# https://www.hackerrank.com/challenges/python-print/problem


def loop_number(n):
    number_is_valid = 1 <= n and n <= 150

    if number_is_valid:
        loop_range = range(1, n + 1)
        string_result = ""

        for i in loop_range:
            string_result += str(i)

        print(string_result)


if __name__ == "__main__":
    n = int(input().strip())
    loop_number(n)