import sys


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    return lines


def make_rotation(current: int, rotation: str):
    direction, amount = rotation[0], int(rotation[1:])

    if direction == "L":
        amount *= -1

    return current + amount


def get_password(rotations):
    current = 50
    p1 = p2 = 0
    was_zero = False
    for rotation in rotations:
        current = value = make_rotation(current, rotation)

        # Special case of 0
        if current == 0:
            p2 += 1

        # Rotation loops around
        elif not (0 <= current <= 99):
            loops = int(current // 100)
            current -= loops * 100
            p2 += abs(loops) + (1 if (not (value % 100) and (value < 0)) else 0)
            if was_zero and value < 0:
                p2 -= 1

        # If rotation stops at multiple of 100, rotations to the left must be discounted
        # by one on the immediate rotation after this. Also, this is p1.
        if not (value % 100):
            was_zero = True
            p1 += 1
        else:
            was_zero = False

    return p1, p2


def main(file_path):
    rotations = read_input(file_path)

    print(get_password(rotations))


if __name__ == "__main__":
    main(sys.argv[1])
