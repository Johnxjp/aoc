from functools import reduce

import sys
from typing import Tuple


def _is_valid_equation(
    target: int,
    values: list[int],
    operations: list[str],
    operator_choice: list[str],
    curr_total: int,
) -> Tuple[bool, list[str]]:

    if curr_total == target and len(values) == 0:
        return True, list(operations)

    if curr_total > target or len(values) == 0:
        return False, []

    next_val = values[0]
    for op in operator_choice:
        if op == "*":
            tot = next_val * curr_total
            new_operations = operations + ["*"]
        else:
            tot = next_val + curr_total
            new_operations = operations + ["+"]

        result, ops = _is_valid_equation(target, values[1:], new_operations, operator_choice, tot)
        if result:
            return True, ops

    return False, []


def is_valid_equation(target: int, values: list[int]) -> Tuple[bool, list[str]]:
    """
    Solved with search. Choose and see if works then try another.

    One way to go about it is to enumerate all possible combinations of
    operators for the length of values we have. There are N - 1 tuples
    and hence N - 1 operators necessary. But because order matters
    the total number of combinations are choose 2 for N - 1 positions.

    possible combinations of operators = 2^N-1

    To reduce search space we could:
    - early stopping, when we have found 1
    - try to see if target is reachable by multiplying all numbers and seeing if smaller

    """
    operators = ["+", "*"]
    N = len(values)
    output = reduce(lambda x, y: x * y, values)
    if output == target:
        return True, ["*"] * (N - 1)

    return _is_valid_equation(target, values[1:], [], operators, values[0])


def apply_operations(values, operations) -> int:
    """ return result """
    total = values[0]
    for v, op in zip(values[1:], operations):
        if op == "*":
            total = total * v
        else:
            total = total + v
    return total
        

def enumerate_all(target, values):
    sequences = [["+"], ["*"]]
    for _ in range(len(values) - 2):
        new_sequences = []
        for op in ["*", "+"]:
            for s in sequences:
                new_sequences.append(s + [op])

        sequences = new_sequences

    for operations in sequences:
        if apply_operations(values, operations) == target:
            return True, operations
    
    return False, []


def p1(target, values) -> int:
    total = 0
    for target, values in data:
        is_valid, _ = is_valid_equation(target, values)
        if is_valid:
            total += target

    return total


if __name__ == "__main__":
    filepath = sys.argv[1]
    data = []
    with open(filepath) as f:
        for line in f:
            target, values = line.strip().split(":")
            values = list(map(int, values.strip().split()))
            data.append((int(target), values))

    print(p1(target, values))
