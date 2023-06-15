import sys
import os


class CopyManager:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def copyfile(self):
        folder = os.path.dirname(__file__)
        content = os.listdir(folder)
        if self.input_file in content:
            with open(self.input_file, mode="rb") as first_file:
                data = first_file.read()
            with open(self.output_file, mode="wb") as second_file:
                second_file.write(data)
        else:
            print("Файл не найден")


copy = CopyManager(input_file=sys.argv[1], output_file=sys.argv[2])
copy.copyfile()
