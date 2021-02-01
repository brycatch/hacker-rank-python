import sys


def get_students_length():
    length = int(input())
    return length


def get_students_string():
    students_string = ""

    for line in sys.stdin:
        if line.rstrip() == "q":
            break
        else:
            students_string += line

    return students_string


def get_students_array(students_string):
    students_array = []
    elements_in_array = students_string.splitlines()

    elements_added_into_students_array = 0
    length_is_valid = len(elements_in_array) % 2 == 0

    if length_is_valid:
        for i in range(1, len(elements_in_array), 2):
            student = [elements_in_array[i - 1], float(elements_in_array[i])]
            students_array.append(student)

    return students_array


def array_length_is_valid(students_array, students_length):
    length = len(students_array)
    return students_length == length and 2 <= length and length <= 5


def sort_students_array(students_array):
    return sorted(students_array, key=lambda x: x[1])


def get_first_lowest_grade(students_array):
    return students_array[0][1]


def get_second_lowest_grade(students_array, first_lowest_grade):
    second_lowest_grade = 0.0

    for student in students_array[1 : len(students_array)]:
        if first_lowest_grade != student[1]:
            second_lowest_grade = student[1]
            break

    return second_lowest_grade


def print_names_of_lowest_grade_students(students_array, second_lowest_grade):
    student_names = [s[0] for s in students_array if s[1] == second_lowest_grade]
    student_names.sort()

    for name in student_names:
        print(name)


if __name__ == "__main__":
    students_length = get_students_length()
    students_string = get_students_string()
    students_array = get_students_array(students_string)

    if array_length_is_valid(students_array, students_length):
        students_array = sort_students_array(students_array)

        second_lowest_grade = get_second_lowest_grade(
            students_array, get_first_lowest_grade(students_array)
        )

        print_names_of_lowest_grade_students(students_array, second_lowest_grade)