import sys


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = f.readlines()

    return [[int(x) for x in line.strip()] for line in lines]


def get_max_joltage(bank: list[int], n: int):
    remaining_batteries = bank
    batteries = []

    for num_remaining_batteries in range(n, 0, -1):

        # Get next battery with highest joltage making sure there are enough batteries
        # for the next selections.
        battery = max(
            remaining_batteries[
                : len(remaining_batteries) - num_remaining_batteries + 1
            ]
        )

        # Remove discarded batteries
        remaining_batteries = remaining_batteries[
            remaining_batteries.index(battery) + 1 :
        ]
        batteries.append(battery)

    return int("".join(str(x) for x in batteries))


def main(file_path):
    banks = read_input(file_path)

    p1 = p2 = 0
    for bank in banks:
        p1 += get_max_joltage(bank, 2)
        p2 += get_max_joltage(bank, 12)

    print(p1, p2)


if __name__ == "__main__":
    main(sys.argv[1])
