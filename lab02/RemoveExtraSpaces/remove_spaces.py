import argparse


def main():
    text = input("Введите текст:")
    print(remove_extra_spaces(text))


def remove_extra_spaces(s):
    return "".join(s.split()) if s is not None else " "


if __name__ == "__main__":
    main()

