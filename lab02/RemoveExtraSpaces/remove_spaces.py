import argparse


def main():
    args: str = "This is Python String"
    print(clear_space(args))


# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("word", type=str, help="Word")
#     args = parser.parse_args()
#     return args


def clear_space(s):
    return "".join(s.split()) if s is not None else " "


if __name__ == "__main__":
    main()

