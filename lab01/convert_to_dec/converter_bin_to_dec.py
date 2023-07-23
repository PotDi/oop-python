import argparse
import sys


def binary_to_int(binary_str) -> int:
    number: int = 0
    for char in binary_str:
        if char not in ["1", "0"]:
            raise ValueError(f"Invalid character '{char}' found")
        number = number * 2 + int(char)
    return number


def main():  # parser можно вынести в отдельную функцию
    binary: str = parse_args()
    try:
        print(binary_to_int(binary))
    except ValueError as e:
        sys.exit(e)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("bin", help="Введите число в двоичной системе")
    args = parser.parse_args()
    b = args.bin
    return b


if __name__ == "__main__":
    main()
