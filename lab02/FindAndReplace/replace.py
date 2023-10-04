import argparse
import io


def open_file(input_file):
    with open(input_file, 'r+', encoding='utf-8') as file:
        text = file.read()
    return text


def write_to_file(input_file, content: str):
    with open(input_file, 'w+', encoding='utf-8') as file:
        file.write(content)


def find_and_replace(input_file, old_text: str, new_text: str):
    text = open_file(input_file)
    new_content = text.replace(old_text, new_text)
    write_to_file(input_file, new_content)


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