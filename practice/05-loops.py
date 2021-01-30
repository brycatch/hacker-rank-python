def square_integer_loop(n):
    number_is_valid = n > 0 and n < 21

    if number_is_valid:
        for i in range(n):
            print(i ** 2)


if __name__ == "__main__":
    n = int(input().strip())
    square_integer_loop(n)