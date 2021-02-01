import builtins
import sys


def get_values_string():
    values_string = ""

    for line in sys.stdin:
        if line.strip() == "q":
            break
        else:
            values_string += line

    return values_string


def convert_values_into_array(values_string):
    return values_string.splitlines()


def get_total_count(values_array):
    total_count = int(values_array.pop(0))
    return total_count, values_array


def validate_tuple_length(elements, total_count):
    is_valid = len(elements) == total_count
    return is_valid


def get_tuple(values_array):
    elements = tuple(map(int, (values_array.pop(0).split())))
    return elements, values_array


def print_hash_by_tuple(elements):
    print(hash(elements))


if __name__ == "__main__":
    values_string = get_values_string()
    values_array = convert_values_into_array(values_string)

    total_count, values_array = get_total_count(values_array)
    elements, values_array = get_tuple(values_array)

    if validate_tuple_length(elements, total_count):
        print_hash_by_tuple(elements)
