import os

file = "matrix.txt"


def open_file():
    folder = os.path.dirname(__file__)
    content = os.listdir(folder)
    if file in content:
        with open(file, mode="rb") as file_name:
            lst = file_name.readlines()
        data = [[float(n) for n in x.split()] for x in lst]
        print(data)
    else:
        print("Файл не найден")



if __name__ == "__main__":
    open_file()
