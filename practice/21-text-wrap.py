import textwrap


def wrap(text, max_width):
    return textwrap.fill(text, max_width)


if __name__ == "__main__":
    text = input()
    max_width = 4
    wrap(text, max_width)