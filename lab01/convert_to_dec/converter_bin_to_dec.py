import argparse


def convert_to_int(b, number: int):
    for i in b:
        number = number*2 + int(i)
    return number


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bin", help="Введите число в двоичной системе")
    args = parser.parse_args()
    b = args.bin
    number: int = 0
    print(convert_to_int(b, number))


if __name__ == "__main__":
    main()

