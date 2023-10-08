def print_transformed_array(numbers, op):
    for n in numbers:
        print(op(n))


def increment(x):
    return x + 1


def square(x):
    return x * x


def main():
    #print_transformed_array([1, 10, 2, 8, 7], square)
    print_transformed_array([1, 10, 2, 8, 7], lambda arg: arg * arg)
    value = int(input("Enter number:"))
    print_transformed_array([1, 10, 2, 8, 7], lambda arg: arg + value)

    def transform_number(number):
        if value != 0:
            return number / value
        else:
            return number

    print_transformed_array([1, 10, 2, 8, 7], transform_number)


if __name__ == "__main__":
    main()


