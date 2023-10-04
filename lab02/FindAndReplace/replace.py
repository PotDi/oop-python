import argparse


def open_file(input_file):
    with open(input_file, 'rs') as file:
        text: str = file.read()


def find_and_replace():
    replace_text = text.replace("wor", "SOS")
    return replace_text


def write_to_file(input_file):
    with open(input_file, 'ws') as file:
        text = file.write()
        return text


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Source file name")
    args = parser.parse_args()
    return args
