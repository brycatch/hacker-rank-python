# https://www.hackerrank.com/challenges/python-lists/problem

import sys


def get_commands_string():
    commands_string = ""

    for line in sys.stdin:
        if line.strip() == "q":
            break
        else:
            commands_string += line

    return commands_string


def get_commands_array(commands_string):
    return str(commands_string).splitlines()


def validate_commands_array(commands_array):
    is_valid = False
    result = []
    commands_length = int(commands_array.pop(0))

    for line in commands_array:
        command = line.split()

        if command[0].strip().lower() == "insert" and len(command) == 3:
            result.append(["insert", int(command[1]), int(command[2])])
        elif command[0].strip().lower() == "print" and len(command) == 1:
            result.append(["print"])
        elif command[0].strip().lower() == "remove" and len(command) == 2:
            result.append(["remove", int(command[1])])
        elif command[0].strip().lower() == "append" and len(command) == 2:
            result.append(["append", int(command[1])])
        elif command[0].strip().lower() == "sort" and len(command) == 1:
            result.append(["sort"])
        elif command[0].strip().lower() == "pop" and len(command) == 1:
            result.append(["pop"])
        elif command[0].strip().lower() == "reverse" and len(command) == 1:
            result.append(["reverse"])

    is_valid = commands_length == len(result)

    return is_valid, result


def create_list_by_commands(commands_array):
    elements = []

    for command in commands_array:
        if command[0] == "insert":
            elements.insert(command[1], command[2])
        elif command[0] == "print":
            print(elements)
        elif command[0] == "remove":
            elements.remove(command[1])
        elif command[0] == "append":
            elements.append(command[1])
        elif command[0] == "sort":
            elements.sort()
        elif command[0] == "pop":
            elements.pop()
        elif command[0] == "reverse":
            elements.reverse()


if __name__ == "__main__":
    commands_string = get_commands_string()
    is_valid, commands_array = validate_commands_array(
        get_commands_array(commands_string)
    )

    if is_valid:
        create_list_by_commands(commands_array)
