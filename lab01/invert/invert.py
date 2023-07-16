import os

import self as self


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


class Matrix3x3:
    def __init__(self):
        self.__items = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def determinant(self, matrix, n) -> int:
        match n:
            case 1:
                return matrix[0][0]
            case 2:
                return matrix[0][0] * matrix[1][1] - matrix[1][0]*matrix[0][1]
            case n:
                for i in range(n):
                    mn = [] #список с дополнительным минором
                    for k in range(n):
                        sm = []
                        for j in range(n):
                            if k != 0 and j != i:
                                sm += [matrix[k][j]]
                        mn += [sm]
                    sm += matrix[0][i] * self.determinant(mn, n - 1) * (-1)**i
                return sm










    # Инвертирует матрицу. В случае успеха возвращает True и изменяет
    # элементы текущей матрицы на инвертированные.
    # Если матрица вырожденная, возврщает False и не меняет элементы матрицы
    def invert(self) -> bool:
        return False

    # Возвращает элемент матрицы в указанном строке и столбце
    def get_at(self, row: int, column: int) -> float:
        return self.__items[row][column]

    def set_at(self, row: int, column: int, value: float):
        self.__items[row][column] = value


def read_matrix3x3(file_name: str) -> Matrix3x3:
    m = Matrix3x3()
    m.set_at(2, 0, 3.1415927)
    return m


def parse_args():
    pass


def print_matrix3x3(m: Matrix3x3):
    for row in range(3):
        for col in range(3):
            print(m.get_at(row, col), end=" ")
        print()


def main():
    args = parse_args()
    m = read_matrix3x3(args.file_name)
    if m.invert():
        print_matrix3x3(m)
    else:
        print("Matrix is singular")


#read = InvertMatrix("matrix.txt")
#read.open_file()
#read.invert_matrix()

m = read_matrix3x3("filename")
print_matrix3x3(m)