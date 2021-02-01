import re


def count_substring(string, sub_string):
    occurrences = [m.start() for m in re.finditer(f"(?={sub_string})", string)]
    return len(occurrences)


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)