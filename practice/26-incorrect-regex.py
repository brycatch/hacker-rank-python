import re
import sys


def get_elements_string():
    elements_string = ""

    for line in sys.stdin:
        if line.strip().lower() == "q":
            break
        else:
            elements_string += line

    return elements_string


def get_elements_array(elements_string):
    elements_string_array = elements_string.splitlines()
    length = int(elements_string_array.pop(0))

    return length, elements_string_array


def validate_regex(elements_array):
    for regex in elements_array:
        try:
            re.compile(regex)
            print(True)
        except re.error:
            print(False)


if __name__ == "__main__":
    elements_string = get_elements_string()
    length, elements_array = get_elements_array(elements_string)

    if length == len(elements_array):
        validate_regex(elements_array)
