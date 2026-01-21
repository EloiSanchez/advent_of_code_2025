import sys


type Tile = tuple[int, int]

def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    red_tiles: list[Tile] = []
    for x, y in [line.split(",") for line in lines]:
        red_tiles.append((int(x), int(y)))

    return red_tiles

def pairwise_areas_max(tiles: list[Tile]):
    max_area = 0
    max_tiles: tuple[Tile, Tile] = ((0, 0), (0,0))
    for idx, tile_1 in enumerate(tiles):
        for tile_2 in tiles[idx + 1:]:
            area = (abs(tile_2[1] - tile_1[1]) + 1) * (abs(tile_2[0] - tile_1[0]) + 1)
            if area > max_area:
                max_area = area
                max_tiles = (tile_1, tile_2)

    return max_area, max_tiles



def main(file_path):
    input = read_input(file_path)

    p1, _ = pairwise_areas_max(input)
    print(p1)



if __name__ == "__main__":
    main(sys.argv[1])
