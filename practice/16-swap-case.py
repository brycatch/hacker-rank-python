def alternate_lower_and_upper(text):
    alternate_text = ""

    for i in text:
        alternate_text += i.lower() if i.isupper() else i.upper()

    return alternate_text


if __name__ == "__main__":
    text = input()
    print(alternate_lower_and_upper(text))