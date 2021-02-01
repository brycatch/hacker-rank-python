import re


def validate_string(text):
    print(bool(re.search("[A-Za-z0-9]", text)))  # alphanumeric
    print(bool(re.search("[A-Za-z]", text)))  # alphabetical
    print(bool(re.search("\d", text)))  # digit
    print(bool(re.search("[a-z]", text)))  # lower
    print(bool(re.search("[A-Z]", text)))  # upper


if __name__ == "__main__":
    text = input()
    validate_string(text)