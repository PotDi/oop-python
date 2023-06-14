import sys


class CopyFile:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def copyfile(self):
        with open(self.input_file, mode="rb") as first_file: #читаем по
            # байтам
            data = first_file.read()
        with open(self.output_file, mode="wb") as second_file: #записываем
            # по байтам
            second_file.write(data)


copy = CopyFile(input_file=sys.argv[1], output_file=sys.argv[2])
copy.copyfile()
