import sys
from copy import deepcopy


def read_input(file_path: str):
    with open(file_path, "r") as f:
        lines = [line for line in f.readlines()]

    # p1
    p1_lines = [[value for value in line.strip().split(" ") if value] for line in lines]
    p1_operations = [[] for _ in range(len(p1_lines[0]))]
    p1_operators = p1_lines[-1]
    for line in p1_lines[:-1]:
        for idx, value in enumerate(line):
            p1_operations[idx].append(int(value))

    # p2
    p2_lines = lines[:-1]
    p2_operators = [x for x in lines[-1][::-1].split(" ") if x.strip()]
    p2_operations = [[] for _ in range(len(p1_lines[0]))]
    # values_start = [[] for _ in range(len(p2_lines))]
    # values = deepcopy(values_start)
    idx = 0
    for chars in zip(*[line[-2::-1] for line in p2_lines]):
        # print(chars)
        if all([char == " " for char in chars]):
            idx += 1
            continue
            # for operation, value_chars in zip(p2_operations, values):
            #     operation.append(int("".join(value_chars)))
            # values = deepcopy(values_start)

        p2_operations[idx].append(int("".join(chars)))
        # print(p2_operations)

    # print(p2_operations)
    # print(p2_operators)

    return p1_operations, p1_operators, p2_operations, p2_operators


def operate(operation: list[int], operator: str):
    if operator == "*":
        total = 1
        for value in operation:
            total *= value
        return total

    elif operator == "+":
        return sum(operation)

    raise ValueError("Operator not recognized")


def main(file_path):
    p1_operations, p1_operators, p2_operations, p2_operators = read_input(file_path)

    p1 = 0
    for operation, operator in zip(p1_operations, p1_operators):
        p1 += operate(operation, operator)

    p2 = 0
    for operation, operator in zip(p2_operations, p2_operators):
        p2 += operate(operation, operator)

    print(p1, p2)


if __name__ == "__main__":
    main(sys.argv[1])
