def print_formatted(limit):
    bin_limit_string = bin(limit)
    width = len(bin_limit_string[2 : len(bin_limit_string)])

    for i in range(1, limit + 1):
        oct_i = oct(i)[2 : len(oct(i))].rjust(width, " ")
        hex_i = hex(i).upper()[2 : len(hex(i))].rjust(width, " ")
        bin_i = bin(i)[2 : len(bin(i))].rjust(width, " ")
        dec_i = str(i).rjust(width, " ")

        print(dec_i, oct_i, hex_i, bin_i)


if __name__ == "__main__":
    limit = int(input())
    print_formatted(limit)