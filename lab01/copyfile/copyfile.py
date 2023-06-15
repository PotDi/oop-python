import sys
import os


class CopyFile:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def copyfile(self):
        folder = os.path.dirname(__file__)
        content = list(filter(lambda x: self.input_file in x, os.listdir(
            folder)))
        file = "".join(map(str, content))
        if self.input_file == file:
            with open(self.input_file, mode="rb") as first_file:
                data = first_file.read()
            with open(self.output_file, mode="wb") as second_file:
                second_file.write(data)
        else:
            print("Файл не найден")


copy = CopyFile(input_file=sys.argv[1], output_file=sys.argv[2])
copy.copyfile()
