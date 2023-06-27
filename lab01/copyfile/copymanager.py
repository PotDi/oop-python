import argparse


def copy_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Source file name")
    parser.add_argument("output_file", type=str, help="Destination file name")
    args = parser.parse_args()
    input_file: str = str(args.input_file)
    output_file: str = str(args.output_file)
    if input_file or output_file is not None:
        with open(input_file, mode="rb") as first_file:
            data = first_file.read()
        with open(output_file, mode="wb") as second_file:
            second_file.write(data)
    else:
        print("Файл не найден")


if __name__ == "__main__":
    copy_file()
