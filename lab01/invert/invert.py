import os


class InvertMatrix:
    def __init__(self, file):
        self.__file = file
        self.__matrix = []

    def open_file(self):
        folder = os.path.dirname(__file__)
        content = os.listdir(folder)
        if self.__file in content:
            with open(self.__file, mode="r") as file_name:
                for i in file_name:
                    lst = [float(n) for n in i.split()]
                    self.__matrix.append(lst)
            print(self.__matrix)
        else:
            print("Файл не найден")

    def invert_matrix(self):
        pass


read = InvertMatrix("matrix.txt")
read.open_file()
