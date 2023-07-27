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


class Matrix3x3:
    def __init__(self):
        self.__items = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def find_determinant(self):
        matrix = self.__items
        try:
            len(matrix) != 3 or len(matrix[0]) != 3
        except ValueError:
            print("Матрица должна быть 3х3")
        det = (matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] *
               matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] *
               matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] -
               matrix[0][1] * matrix[1][0] * matrix[2][2] - matrix[0][0] *
               matrix[1][2] * matrix[2][1])
        return det

    # Инвертирует матрицу. В случае успеха возвращает True и изменяет
    # элементы текущей матрицы на инвертированные.
    # Если матрица вырожденная, возврщает False и не меняет элементы матрицы
    def invert(self) -> bool:
        matrix = self.__items
        deter = self.find_determinant()
        if deter == 0:
            return False
        self.__items = [[(matrix[1][1] * matrix[2][2] - matrix[1][2]
                          * matrix[2][1]) / deter, (matrix[0][2] *
                                                    matrix[2][1] -
                                                    matrix[0][1] *
                                                    matrix[2][2]) / deter,
                         (matrix[0][1] * matrix[1][2] - matrix[0][2]
                          * matrix[1][1]) / deter], [(matrix[1][2] *
                                                      matrix[2][0] -
                                                      matrix[1][0] *
                                                      matrix[2][2])
                                                     / deter,
                                                     (matrix[0][0] *
                                                      matrix[2][2] -
                                                      matrix[0][2]
                                                      * matrix[2][
                                                          0]) / deter,
                                                     (matrix[0][2] *
                                                      matrix[1][0] -
                                                      matrix[0][0] *
                                                      matrix[1][2]) /
                                                     deter,
                                                     (matrix[0][2] *
                                                      matrix[1][0] -
                                                      matrix[0][0] *
                                                      matrix[1][2])
                                                     / deter],
                        [(matrix[1][0] * matrix[2][1] - matrix[1][1]
                          * matrix[2][0]) / deter, (matrix[0][1] *
                                                    matrix[2][0] -
                                                    matrix[0][0] *
                                                    matrix[2][1])
                         / deter, (matrix[0][0] * matrix[1][1] -
                                   matrix[0][1] * matrix[1][0]) / deter]]
        return True

    # Возвращает всю матрицу
    def get_matrix(self) -> list[list[float]]:
        return self.__items

    # def get_at(self, row: int, column: int) -> float:
    #     return self.__items[row][column]

    # def set_at(self, row: int, column: int, value: float):
    #     self.__items = value


def read_matrix3x3(file_name: str) -> Matrix3x3:
    m = Matrix3x3()
    m.get_matrix()
    return m


def parse_args():
    pass


def print_matrix3x3(m: Matrix3x3):
    matrix = m.get_matrix()
    for row in range(3):
        for col in range(3):
            print(matrix[row][col], end=" ")
        print()


def main():
    args = parse_args()
    m = read_matrix3x3(args.file_name)
    if m.invert():
        print_matrix3x3(m)
    else:
        print("Matrix is singular")


# read = InvertMatrix("matrix.txt")
# read.open_file()
# read.invert_matrix()


m = read_matrix3x3("filename")
print_matrix3x3(m)
