import sys
import re
from collections import OrderedDict


def get_elements_string():
    elements_string = ""

    for line in sys.stdin:
        if line.strip().lower() == "q":
            break
        else:
            elements_string += line

    return elements_string


def get_elements_array(elements_string):
    elements = []
    regex = "([A-Za-z\s]*)\s(\d{1,})"

    elements_string_array = elements_string.splitlines()
    length = int(elements_string_array.pop(0))

    for element in elements_string_array:
        result = re.findall(regex, element, re.I).pop(0)
        elements.append([result[0], int(result[1])])

    return length, elements


def create_dictionary(elements_array):
    ordered_dictionary = OrderedDict()

    for element in elements_array:
        if str(element[0]) in ordered_dictionary:
            ordered_dictionary[str(element[0])] += int(element[1])
        else:
            ordered_dictionary[str(element[0])] = int(element[1])

    return ordered_dictionary


def print_dictionary(dictionary):
    for key in dictionary:
        print(f"{key} {dictionary[key]}")


if __name__ == "__main__":
    elements_string = get_elements_string()
    length, elements_array = get_elements_array(elements_string)

    if length == len(elements_array):
        dictionary = create_dictionary(elements_array)
        print_dictionary(dictionary)
