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