# https://www.hackerrank.com/challenges/hackerrank-language/problem
import re
import sys


def main():
    request = get_request()
    validate_request(request)


def get_request():
    request = ""
    for line in sys.stdin:
        if line.rstrip() == "q":
            break
        else:
            request += line
    return request


def validate_request(request):
    request_regex = "^(\d{5})\s(.*)$"
    language_regex = "^C$|^CPP$|^JAVA$|^PYTHON$|^PERL$|^PHP$|^RUBY$|^CSHARP$|^HASKELL$|^CLOJURE$|^BASH$|^SCALA$|^ERLANG$|^CLISP$|^LUA$|^BRAINFUCK$|^JAVASCRIPT$|^GO$|^D$|^OCAML$|^R$|^PASCAL$|^SBCL$|^DART$|^GROOVY$|^OBJECTIVEC$"

    # Get an array with the lines in the request
    lines_in_request = re.findall("(.*[^\s])", request, re.I)
    # Get constraint N
    n = int(lines_in_request.pop(0))

    # For into languages received
    for i in range(n):
        # Get api_id and language from line
        request_string = re.findall(request_regex, lines_in_request[i], re.I).pop()
        api_id = int(request_string[0])
        language = request_string[1]

        # Validate constraints
        api_id_is_valid = api_id >= 10000 and api_id <= 100000
        language_is_valid = bool(re.match(language_regex, language))

        is_valid = api_id_is_valid and language_is_valid

        # Get and print message
        message = "VALID" if is_valid else "INVALID"
        print(message)


if __name__ == "__main__":
    main()
