# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def create_score_array(score_string, score_array_length):
    score_array = [int(i) for i in score_string.split()]
    score_array = score_array[0:score_array_length]
    score_array.sort(reverse=True)
    return score_array


def length_is_valid(score_array_length):
    return 2 <= score_array_length and score_array_length <= 10


def array_is_valid(score_array):
    is_valid = True

    for i in score_array:
        if not (-100 <= i and i <= 100):
            is_valid = False
            break

    return is_valid


def find_runner_up_score(score_array):
    first_place = score_array.pop(0)
    second_place = 0

    for i in score_array:
        if i < first_place:
            print(i)
            break


if __name__ == "__main__":
    score_array_length = int(input())
    score_string = input()

    if length_is_valid(score_array_length):
        score_array = create_score_array(score_string, score_array_length)

        if array_is_valid(score_array):
            find_runner_up_score(score_array)
