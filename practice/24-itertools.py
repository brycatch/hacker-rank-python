from itertools import product


def get_array_element():
    first_element = list(map(int, input().split()))
    return first_element


def print_product(first_element, second_element):
    product_list_string = str(list(product(first_element, second_element))).replace(
        "),", ")"
    )
    print(product_list_string[1 : len(product_list_string) - 1])


if __name__ == "__main__":
    first_element = get_array_element()
    second_element = get_array_element()

    print_product(first_element, second_element)
