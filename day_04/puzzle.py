import sys

DIRECTIONS = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    return [[x for x in line] for line in lines]


def is_accessible(map: list[list[str]], position: tuple[int, int]) -> bool:

    y, x = position
    adjacent = 0

    for direction in DIRECTIONS:
        n_y, n_x = (y + direction[0], x + direction[1])
        if (n_y >= 0) and (n_x >= 0):

            try:
                if map[n_y][n_x] == "@":
                    adjacent += 1

            except IndexError:
                pass

    return adjacent < 4


def find_accessible(map: list[list[str]]):
    rows, columns = len(map), len(map[0])

    counter = 0
    accessible = []

    # For each positin
    for i in range(rows):
        for j in range(columns):

            position = (i, j)

            # If it's a barrel and it's accessible, mark it as accessible
            if map[i][j] == "@" and is_accessible(map, position):
                counter += 1
                accessible.append((i, j))
    return counter, accessible


def main(file_path):
    map = read_input(file_path)

    # P1
    p1, _ = find_accessible(map)

    # P2
    removed = -1
    p2 = 0
    # Find accessible barrels and remove them until no new barrels are found
    while removed != 0:
        removed, accessible = find_accessible(map)
        p2 += removed
        for i, j in accessible:
            map[i][j] = "x"
    print(p1, p2)


if __name__ == "__main__":
    main(sys.argv[1])
