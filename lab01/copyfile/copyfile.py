import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, encoding="UTF-8") as first_file:
    data = first_file.read()

with open(output_file, mode="w", encoding="UTF-8") as second_file:
        second_file.write(data)
