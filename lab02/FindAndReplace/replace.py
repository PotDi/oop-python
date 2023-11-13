def open_file(input_file): #переименовать функцию в read_file
    with open(input_file, 'r+', encoding='utf-8') as file:
        text = file.read() #считывание должно строка за строкой, а не весь
        # файл целиком
    return text


def write_to_file(input_file, content: str):
    with open(input_file, 'w+', encoding='utf-8') as file:
        file.write(content)


def find_and_replace(text: str, text_to_find: str, replacement_text: str) \
        -> str:
    found_pos = text.find(text_to_find)
    if found_pos == -1:
        return text
    return text[0:found_pos] + replacement_text + text[found_pos + len(
        text_to_find):]


def find_and_replace_in_file(input_file, old_text: str, new_text: str):
    text = open_file(input_file)
    new_content = text.replace(old_text, new_text)
    write_to_file(input_file, new_content)
# вывод в стандартный поток вывода(в консоль) и написать тест sys.stdin