import sys
import math
from typing import overload

type coord = tuple[int, int, int]

def read_input(file_path: str) -> list[tuple[int ,int , int]]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    values = []
    for line in lines:
        coord = line.split(",")
        values.append(tuple(int(c) for c in coord))

    return values

def find_distances(coords: list[coord]):
    distances = []
    for idx, coord_1 in enumerate(coords):
        for coord_2 in coords[idx + 1 :]:
            dist = math.dist(coord_1, coord_2)
            distances.append((coord_1, coord_2, dist))

    return sorted(distances, key=lambda x: x[2])

def merge(coord_to_merge: coord, circuit, circuits):
    for idx, circuit_2 in enumerate(circuits):
        if coord_to_merge in circuit_2:
            circuits.pop(idx)
            circuit.extend(circuit_2)
            return

@overload
def find_connections_or_last(
        coords: list[coord], sorted_coords: list[tuple[coord, coord, float]], n_connections: None
        ) -> tuple[coord, coord]: ...

@overload
def find_connections_or_last(
        coords: list[coord], sorted_coords: list[tuple[coord, coord, float]], n_connections: int
        ) -> list[tuple[list[coord], int]]: ...


def find_connections_or_last(
        coords: list[coord], sorted_coords: list[tuple[coord, coord, float]], n_connections: int | None
        ) -> list[tuple[list[coord], int]] | tuple[coord, coord]:

    if not n_connections:
        n_connections = len(sorted_coords)

    # All nodes are a circuit at the beginning
    circuits = [[coord] for coord in coords]

    for coord_1, coord_2, _ in sorted_coords[:n_connections]:
        for circuit in circuits:

            # if coord in circuit
            is_1_in = coord_1 in circuit
            is_2_in = coord_2 in circuit
            if is_1_in or (is_2_in):

                # if both in circuit, skip
                if is_1_in and is_2_in:
                    break

                # else, merge other to circuit
                elif is_1_in:
                    merge(coord_2, circuit, circuits)
                elif is_2_in:
                    merge(coord_1, circuit, circuits)

            # for p2, if all circuits merged, return last coordinates
            if len(circuits) == 1:
                return coord_1, coord_2

    # for p1, return circuits and their lengths for later sorting
    return [(circuit, len(circuit)) for circuit in circuits]


def size_top_circuits(circuits, top):
    value = 1
    for circuit in sorted(circuits, key=lambda x: x[1], reverse=True)[:top]:
        value *= circuit[1]
    return value


def main(file_path):
    coords = read_input(file_path)

    p1, p2 = 0, 0
    sorted_coords = find_distances(coords)

    circuits = find_connections_or_last(coords, sorted_coords, 1000)
    p1 = size_top_circuits(circuits, 3)


    last_coord_1, last_coord_2 = find_connections_or_last(coords, sorted_coords, None)
    p2 = last_coord_1[0] * last_coord_2[0]

    print(p1, p2)



if __name__ == "__main__":
    main(sys.argv[1])
