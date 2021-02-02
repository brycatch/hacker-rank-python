def solve(s):
    array_names = s.split()
    for i in range(len(array_names)):
        array_names[i] = array_names[i].capitalize()

    result = " ".join(array_names)

    return result


if __name__ == "__main__":

    s = input()
    result = solve(s)

    print(result)
