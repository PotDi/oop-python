import argparse
from replace import find_and_replace


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Source file name")
    parser.add_argument("old_text", type=str, help="Old string in text")
    parser.add_argument("new_text", type=str, help="New string in text")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    find_and_replace(args.input_file, args.old_text, args.new_text)


if __name__ == "__main__":
    main()
