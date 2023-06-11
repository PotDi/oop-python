import sys


class CopyFile:
    def __init__(self):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]

    def copyfile(self):
        with open(self.input_file, encoding="UTF-8") as first_file:
            data = first_file.read()
        with open(self.output_file, mode="w",
                  encoding="UTF-8") as second_file:
            second_file.write(data)


copy = CopyFile()
copy.copyfile()
