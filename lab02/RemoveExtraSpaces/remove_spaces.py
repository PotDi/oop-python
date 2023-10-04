import argparse


def main():
    text = input("Введите текст:")
    print(clear_space(text))


def clear_space(s):
    return "".join(s.split()) if s is not None else " "


if __name__ == "__main__":
    main()

