"""
antenna tuned to frequency -> lower case letter, uppercase or digit
antinodes
- two atennas same frequency but antenna twice as far
- straight line (horizontal, vertical, diagonal)
- antinodes are on each side of pair of atennas

1. Find pairs of atennas same frequency.
2. Determine the space between them and if it's a line. There is always a line
 - line defined by dx, dy
3. Antinodes at (A1 + dy, A1 + dx) and (A2 + dy, A2 + dx).
4. Check for signs when adding increments.
5. Check for out of bounds
6. Check for obstacles (include conflicts with other locations)

7. Output unique antinode locations. So track antinode locations in set

Step 3 is the critical addition. When is dy, dx postivie or negative.

Algorithm:

1. Find all locations of same frequency
2. Find all unique pairs. Order not important
3. Find line between them
4. Find antinodes. Store antinodes in set
5. Output Set.

2. unique pairs. Just do this with two pointers.
3. change in x, change in y. Challenge for me. Which one to apply negative dx, dy to?
    If A1 - A2 = dx, dy, then you have arrow from A2 -> A1. So A1 + dx, dy. A2 - dx, dy

"""

import sys
from typing import Tuple, Set
from collections import defaultdict


def load_data(filename: str) -> list[str]:
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(line.strip())
    return grid


def find_frequency_locations(grid) -> dict[str, list[Tuple[int, int]]]:
    locs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = grid[i][j]
            if c != ".":
                locs[c].append((i, j))

    return locs


def get_all_pairs(
    frequency_locs: list[Tuple[int, int]],
) -> list[Tuple[Tuple[int, int], Tuple[int, int]]]:
    pair_combos = []
    for i, p1 in enumerate(frequency_locs):
        for p2 in frequency_locs[i + 1 :]:
            pair_combos.append((p1, p2))
    return pair_combos


def get_antinode_locs(
    frequency_pair: Tuple[Tuple[int, int], Tuple[int, int]],
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Takes a pair in and returns two antinode locs valid or not"""
    p1, p2 = frequency_pair
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (p1[0] + dx, p1[1] + dy), (p2[0] - dx, p2[1] - dy)


def get_all_antinode_locs(
    frequency_pair: Tuple[Tuple[int, int], Tuple[int, int]], nrows: int, ncols: int
) -> list[Tuple[Tuple[int, int], Tuple[int, int]]]:
    p1, p2 = frequency_pair
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    antinode_locs = set()
    a = (p1[0], p1[1])
    while is_valid_loc(a, nrows, ncols):
        antinode_locs.add(a)
        a = (a[0] + dx, a[1] + dy)

    a = (p2[0], p2[1])
    while is_valid_loc(a, nrows, ncols):
        antinode_locs.add(a)
        a = (a[0] - dx, a[1] - dy)

    return antinode_locs


def is_valid_loc(antinode_loc: Tuple[int, int], nrows: int, ncols: int) -> bool:
    x, y = antinode_loc
    if x < 0 or x >= nrows or y < 0 or y >= ncols:
        return False
    return True


def main(filename: str):
    data: list[str] = load_data(filename)
    locs = find_frequency_locations(data)
    antinode_locs: Set[Tuple[int, int]] = set()
    nrows = len(data)
    ncols = len(data[0])
    for k, v in locs.items():
        k_pairs = get_all_pairs(v)
        for pair in k_pairs:
            a1, a2 = get_antinode_locs(pair)
            if is_valid_loc(a1, nrows, ncols):
                antinode_locs.add(a1)
            if is_valid_loc(a2, nrows, ncols):
                antinode_locs.add(a2)

    print(len(antinode_locs))

    # Part 2
    antinode_locs: Set[Tuple[int, int]] = set()
    for k, v in locs.items():
        k_pairs = get_all_pairs(v)
        for pair in k_pairs:
            resonant_pairs = get_all_antinode_locs(pair, nrows, ncols)
            antinode_locs = antinode_locs.union(resonant_pairs)

    print(len(antinode_locs))


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
