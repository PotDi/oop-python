import os


class InvertMatrix:
    def __init__(self, file):
        self.file = file
        self.matrix = []

    def open_file(self):
        folder = os.path.dirname(__file__)
        content = os.listdir(folder)
        if self.file in content:
            with open(self.file, mode="r") as file_name:
                for i in file_name:
                    lst = [float(n) for n in i.split()]
                    self.matrix.append(lst)
            print(self.matrix)
        else:
            print("Файл не найден")

    def invert_matrix(self):
        pass


read = InvertMatrix("matrix.txt")
read.open_file()
# if __name__ == "__main__":
#     InvertMatrix.open_file()
