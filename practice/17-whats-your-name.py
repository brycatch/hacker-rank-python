def print_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}! You just delved into python.")


def validate_names(first_name, last_name):
    first_name_len = len(first_name)
    last_name_len = len(last_name)

    first_name_is_valid = 0 < first_name_len and first_name_len <= 10
    last_name_is_valid = 0 < last_name_len and last_name_len <= 10

    return first_name_is_valid and last_name_is_valid


if __name__ == "__main__":
    first_name = input()
    last_name = input()

    if validate_names(first_name, last_name):
        print_full_name(first_name, last_name)