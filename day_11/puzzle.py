import sys
from typing import Deque

# aaa: you hhh


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    routers = {}
    for line in lines:
        source, destinations = line.split(":")
        routers[source.strip()] = [x.strip() for x in destinations.split()]

    return routers


def count_paths(routers: dict[str, list[str]]):

    count = 0
    deque = Deque([(node, ["svr"]) for node in routers.pop("svr")])
    while deque:
        new_node, previous_path = deque.popleft()
        new_destinations = routers[new_node].copy()
        for new_destination in new_destinations:
            if new_destination != "out":
                if new_destination not in previous_path[::-1]:
                    print(len(previous_path))
                    deque.appendleft((new_destination, previous_path + [new_node]))
                else:
                    print("Found in path")
            else:
                # if "fft" in previous_path and "dac" in previous_path:
                count += 1
            print(len(deque))
    return count


def main(file_path):
    routers = read_input(file_path)

    p1 = count_paths(routers)

    print(p1)


if __name__ == "__main__":
    main(sys.argv[1])
