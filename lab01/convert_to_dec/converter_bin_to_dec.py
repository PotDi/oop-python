import argparse


def convert_to_int(b, number: int) -> int:
    for i in b:
        number = number*2 + int(i)
    return number


def main(): # parser можно вынести в отдельную функцию
    b = parse_args()
    number: int = 0
    print(convert_to_int(b, number))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("bin", help="Введите число в двоичной системе")
    args = parser.parse_args()
    b = args.bin
    return b


if __name__ == "__main__":
    main()

