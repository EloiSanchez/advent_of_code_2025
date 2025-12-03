import sys


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = f.readlines()

    return [x.split("-") for x in lines[0].strip().split(",")]


# Overoptimized so it only works for P1
def add_invalid_ids_in_range(id_range: list[str]):
    start, end = id_range

    if len(start) % 2:
        # When ranges do not include possible invalid ids (even length)
        if len(start) == len(end):
            return 0

        # Round start to first even digited product id
        start = "1" + "0" * len(str(start))

    if len(end) % 2:
        # Round end to last even digited product id
        end = "9" * (len(end) - 1)

    # Create subsets of ranges to skip over odd digited product ids
    working_ranges = []
    while int(start) < int(end):
        new_end = "9" * len(start)
        if int(new_end) > int(end):
            new_end = end

        working_ranges.append([start, new_end])
        start = "1" + "0" * (len(start) + 1)

    # Actual checking of product_ids
    result = 0
    for start, end in working_ranges:
        for value in range(int(start), int(end) + 1):
            value_str = str(value)
            len_value = len(value_str)
            if value_str[: int(len_value // 2)] == value_str[int(len_value // 2) :]:
                result += value

    return result


def is_repeating(product_id_str: str, pattern_len: int):

    # Length of value must be multiple of pattern length to be invalid
    if len(product_id_str) % pattern_len:
        return False

    # If check if there is repetition
    remaining = product_id_str[pattern_len:]
    pattern = product_id_str[:pattern_len]
    while len(remaining) >= pattern_len:

        # If not repeating, exit
        if remaining[:pattern_len] != pattern:
            return False

        # Else, continue with remaining of value
        remaining = remaining[pattern_len:]

    # If repeating for the whole string
    return True


def is_invalid(product_id: int):
    product_id_str = str(product_id)

    for pattern_len in range(int(len(product_id_str) // 2), 0, -1):

        # If found repeating pattern of length pattern_len then it is invalid
        if is_repeating(product_id_str, pattern_len):
            return True

    # If no pattern of any lenght is found then it is valid
    return False


def add_repeating_patterns(id_range):
    start, end = id_range

    # Iterate over product ids in range
    results = 0
    for product_id in range(int(start), int(end) + 1):

        # If product_id is invalid, add it to results
        if is_invalid(product_id):
            results += product_id

    return results


def main(file_path):
    product_ids = read_input(file_path)

    p1 = p2 = 0
    for id_range in product_ids:
        p1 += add_invalid_ids_in_range(id_range)
        p2 += add_repeating_patterns(id_range)

    print(p1, p2)


if __name__ == "__main__":
    main(sys.argv[1])
