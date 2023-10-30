"""
Написать программу, которая построчно обрабатывает текстовый файл и при этом
выполняет над ним некоторые манипуляяции
1. Удаляет из каждой строки файла некоторое слово и результат записывает в
выходной файл
proces-file.py remove input.txt output.txt shit
Из каждой строки удаляется слово shit. Последовательность символов shit
внутри других слов удаляться не должна.

2. Заменяет из каждой строки файла искомое слово на слово-заменитель и
записывает результат в выходной файл
process-file.py replace input.txt output.txt shit candy
Заменяет в каждой строке слово shit на candy

3. Подсчитывает количество слов в файле. В конце выводит количество слов на консоль
process-file.py count-words input.txt
Подсчитывает количество слов в input.txt

4. Изменяет порядок слов каждой строке на противоположный и результат
записывает в выходной файл
подстроки в строке
process-file.py reverse-lines input.txt output.txt
Заменяет порядок слов в каждой строке на противоположный
5. Есть строка, считывает строк и выводит гласные буквы английского языка.
a, e, o, u, i, y вне зависимости от регистра

"""


def process_file(file_name: str, transformer):
    pass


def remove_word(text: str, word: str) -> str:
    pass


def remove_word_from_file(input_file_name:str, out_file_name: str, word: str):
    """


    with open(out_file_name) as out_file:

        # Будет вызываться из функции process_file для каждой строки
        # входного файла
        def remover(text: str):
            text = remove_word(text, word)
            write(out_file, text)

        process_file(input_file, remover)
    """

"""


"""