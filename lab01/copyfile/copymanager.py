import argparse


def main():
    args = parse_args()
    copy_file(args.input_file, args.output_file)


def copy_file(input_file: str, output_file: str):
    with open(input_file, mode="rb") as first_file:
        data = first_file.read()
    with open(output_file, mode="wb") as second_file:
        second_file.write(data)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Source file name")
    parser.add_argument("output_file", type=str, help="Destination file name")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
