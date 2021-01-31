# https://www.hackerrank.com/challenges/finding-the-percentage/problem
import re
import sys


class Student:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def get_average(self):
        result = 0
        for value in self.values:
            result += value

        return result / 3


def main():
    # Get lines from console
    lines = get_lines()

    # Get total students (n)
    n = get_total(lines)

    # Get name to find him
    name = get_name_to_find(lines)

    # Get students
    students = get_students(lines, n)

    # Find name in students, if find him, make average
    find_student_and_make_average(students, name)


def get_lines():
    lines = ""
    for line in sys.stdin:
        if line.rstrip() == "q":
            break
        else:
            lines += line
    return lines


def get_total(lines):
    result = re.findall("(.*[^\s])", lines, re.I)
    return int(result.pop(0))


def get_name_to_find(lines):
    result = re.findall("(.*[^\s])", lines, re.I)
    return result.pop(-1)


def get_students(lines, n):
    students = []
    regex = "([A-Za-z]*) (.*)"
    regex_result = re.findall("(.*[^\s])", lines, re.I)

    students_lines_array = regex_result[1:-1]

    for i in range(n):
        result = re.findall(regex, students_lines_array[i], re.I).pop(0)
        name = result[0]
        values = map(float, result[1].split())
        students.append(Student(name, values))

    return students


def find_student_and_make_average(students, name):

    for s in students:
        if s.name.lower() == name.lower():
            print("{:.2f}".format(s.get_average()))


if __name__ == "__main__":
    main()