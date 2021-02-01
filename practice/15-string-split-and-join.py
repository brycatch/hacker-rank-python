def split_string(text, delimiter=""):
    return delimiter.join(text.split())


if __name__ == "__main__":
    text = input()
    print(split_string(text, "-"))
