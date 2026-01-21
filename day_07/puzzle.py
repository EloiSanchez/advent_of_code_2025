from collections import defaultdict, deque
from functools import lru_cache
import sys


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    ray = (0, 0)
    splitters = []
    for i, line in enumerate(lines):
        for j, value in enumerate(line):
            if value == "S":
                ray = (i, j)
            elif value == "^":
                splitters.append((i, j))
    return (
        tuple(splitters),
        ray,
        len(lines),
        len(lines[0]),
        [[x for x in line] for line in lines],
    )


@lru_cache(None)
def iterate_ray(
    ray: tuple[int, int],
    splitters: tuple[tuple[int, int]],
    max_length: int,
    max_width: int,
):

    (i, j) = pos = ray
    while True:
        if not (0 <= j < max_width):
            # print(f"too far to the side at {(i, j)}")
            return 1

        if i >= max_length:
            # print(f"reached end at {(i, j)}")
            # timelines += 1
            return 1

        if pos in splitters:
            # print(f"found splitter at {(i, j)}")
            # map[pos[0]][pos[1]] = "o"
            return iterate_ray(
                (i, j + 1), splitters, max_length, max_width
            ) + iterate_ray((i, j - 1), splitters, max_length, max_width)

        else:
            # map[pos[0]][pos[1]] = "|"
            i, j = pos = (i + 1, j)


def iterate_map(
    ray: tuple[int, int],
    # map: list[list[str]],
    splitters: tuple[tuple[int, int]],
    max_length: int,
    max_width: int,
    is_p2: bool = False,
):
    queue = deque([ray])

    count = 0
    seen = []
    # found = defaultdict(lambda: 0)
    # timelines = 0
    while queue:
        (i, j) = pos = queue.popleft()

        if (pos in seen) and (not is_p2):
            continue

        if not is_p2:
            seen.append(pos)
        # print(i, j)

        result = iterate_ray(pos, splitters, max_length, max_width)
        print(result)

        # if result:
        #     count += 1
        #     for new in result:
        #         if is_p2:
        #             queue.appendleft(new)
        #         else:
        #             queue.append(new)

    # for node, visited in found.items():
    #     print(node, visited)
    # for line in map:
    #     print("".join(line))
    # print()

    # if not is_p2:
    return count + 1

    # return sum(found.values())


def main(file_path):
    splitters, ray, max_length, max_width, map = read_input(file_path)

    p1, p2 = 0, 0
    # print(splitters)
    # p1 = iterate_map(ray, map, max_length, max_width)

    p2 = iterate_map(ray, splitters, max_length, max_width, True)
    print(p1, p2)


if __name__ == "__main__":
    main(sys.argv[1])
