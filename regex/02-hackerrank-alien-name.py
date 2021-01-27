# https://www.hackerrank.com/challenges/alien-username/problem

import re
import sys


def main():
    request = get_alien_names()
    validate_alien_names(request)


def get_alien_names():
    request = ""
    for line in sys.stdin:
        if line.rstrip() == "q":
            break
        else:
            request += line
    return request


def validate_alien_names(request):
    name_regex = "^([\.\_][0-9]+[A-Za-z]*\_?)$"

    # Get an array with the lines in the request
    alien_names = re.findall("(.*[^\s])", request, re.I)
    # Get constraint N
    n = int(alien_names.pop(0))

    # For into languages received
    for i in range(n):
        # Get api_id and language from line
        alien_name_is_valid = bool(re.match(name_regex, alien_names[i], re.I))
        # Get and print message
        message = "VALID" if alien_name_is_valid else "INVALID"
        print(message)


if __name__ == "__main__":
    main()
