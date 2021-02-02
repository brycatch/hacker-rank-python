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


def validate_divisions(elements_array):
    for elements in elements_array:
        try:
            operators = elements.split()
            print(int(operators[0]) // int(operators[1]))
        except ValueError as e:
            print(f"Error Code: {e}")
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")


if __name__ == "__main__":
    elements_string = get_elements_string()
    length, elements_array = get_elements_array(elements_string)

    if length == len(elements_array):
        validate_divisions(elements_array)
