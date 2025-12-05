import sys


def read_input(file_path: str) -> tuple[list[list[int]], list[int]]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    section_1 = True
    fresh_ranges, product_ids = [], []
    for line in lines:
        if section_1:

            if not line:
                section_1 = False
                continue

            fresh_ranges.append([int(x) for x in line.split("-")])

        else:
            product_ids.append(int(line))

    return fresh_ranges, product_ids


def is_fresh(product_id: int, fresh_ranges: list[list[int]]):
    for start, end in fresh_ranges:
        if start <= product_id <= end:
            return True

    return False


def merge_ranges(range_1: list[int], range_2: list[int]) -> bool:
    # range_1 := []
    # range_2 := ()

    start, end = range_1

    if range_2[0] <= start <= range_2[1]:

        # (  [  )   ]
        if range_2[1] <= end:
            range_2[1] = end

        # else: (  [ ]  )

        return True

    elif range_2[0] <= end <= range_2[1]:

        # [  (  ]  )
        if start <= range_2[0]:
            range_2[0] = start

        return True

    # [  (  )  ]
    elif start <= range_2[0] and range_2[1] <= end:
        range_2[0], range_2[1] = start, end

        return True

    return False


def count_all_fresh_ids(fresh_ranges: list[list[int]]):

    to_drop = []

    # Iterate over all ranges once keeping track of their position
    for idx, fresh_range in enumerate(fresh_ranges):

        # Compare with the remaining ranges in the list
        for working_range in fresh_ranges[idx + 1 :]:

            # If range is mergeable with another range, merge it in place and remember
            # to not count it later, since it's already taken into account in the other
            # range
            if merge_ranges(fresh_range, working_range):
                to_drop.append(idx)
                break

    count = 0
    # Count amount of values in each range...
    for idx, (start, end) in enumerate(fresh_ranges):

        # ...keeping in mind not to count dropped ones
        if idx not in to_drop:
            count += end - start + 1

    return count


def main(file_path):
    fresh_ranges, product_ids = read_input(file_path)

    p1 = sum(is_fresh(product_id, fresh_ranges) for product_id in product_ids)
    p2 = count_all_fresh_ids(fresh_ranges)

    print(p1, p2)


if __name__ == "__main__":
    main(sys.argv[1])
