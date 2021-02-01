import sys


def get_lines_from_command():
    lines_string = ""
    length = 0

    for line in sys.stdin:
        lines_string += line
        length += 1
        if length > 3:
            break

    return lines_string


def convert_lines_into_array(values_string):
    return values_string.splitlines()


def convert_array_by_string(values_array):
    elements = list(map(int, values_array.pop(0).split()))
    return elements, values_array


def get_n_m_array(values_array):
    n_m_array, values_array = convert_array_by_string(values_array)
    return n_m_array, values_array


def get_values_to_compare(values_array):
    values_to_compare, values_array = convert_array_by_string(values_array)
    return values_to_compare, values_array


def get_like_set(values_array):
    like_set, values_array = convert_array_by_string(values_array)
    return like_set, values_array


def get_dislike_set(values_array):
    dislike_set, values_array = convert_array_by_string(values_array)
    return dislike_set, values_array


def validate_arrays(n_m_array, values_to_compare, like_set, dislike_set):
    is_valid = False

    n = n_m_array.pop(0)
    m = n_m_array.pop(0)

    n_is_valid = 1 <= n and n <= 10 ** 5
    m_is_valid = 1 <= m and m <= 10 ** 5

    if not (n_is_valid and m_is_valid):
        return False

    values_is_valid = len(values_to_compare) == n
    like_is_valid = len(like_set) == m
    dislike_is_valid = len(dislike_set) == m

    is_valid = values_is_valid and like_is_valid and dislike_is_valid

    return is_valid


def intersection(first_array, second_array):
    temp_array = set(second_array)
    result = [value for value in first_array if value in temp_array]
    return result


def get_count_of_like_set(values_to_compare, like_set, happiness):
    like_count = len(intersection(values_to_compare, like_set))
    happiness += like_count
    return happiness


def get_count_of_dislike_set(values_to_compare, dislike_set, happiness):
    dislike_count = len(intersection(values_to_compare, dislike_set))
    happiness -= dislike_count
    return happiness


def print_result(happiness):
    print(happiness)


if __name__ == "__main__":
    values_string = get_lines_from_command()
    values_array = convert_lines_into_array(values_string)

    n_m_array, values_array = get_n_m_array(values_array)
    values_to_compare, values_array = get_values_to_compare(values_array)
    like_set, values_array = get_like_set(values_array)
    dislike_set, values_array = get_dislike_set(values_array)

    if validate_arrays(n_m_array, values_to_compare, like_set, dislike_set):
        happiness = 0
        happiness = get_count_of_like_set(values_to_compare, like_set, happiness)
        happiness = get_count_of_dislike_set(values_to_compare, dislike_set, happiness)
        print_result(happiness)
