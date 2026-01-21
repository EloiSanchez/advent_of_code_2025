import sys


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = f.readlines()

    return lines


def main(file_path):
    input = read_input(file_path)


if __name__ == "__main__":
    main(sys.argv[1])
