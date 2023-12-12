def read_dict(path):
    dictionary = {}
    with open(path, 'r') as file:
        for line in file:
            key, value = map(str.strip, line.split(':'))
            dictionary[key] = value
        return dictionary


def translate_word(word, dictionary):
    translation = dictionary.get(word.lower())
    if translation:
        return translation
    else:
        return "Перевод не найден"


def write_dict(path, word, translation):
    with open(path, 'a') as file:
        file.write(f'{word}:{translation}\n')
    print(f"Слово '{word}' с переводом '{translation}' успешно добавлен в "
          f"словарь")

