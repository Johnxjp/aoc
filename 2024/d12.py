from operator import itemgetter
from typing import Tuple


def load_grid(filename: str):
    grid = []
    with open(filename) as f:
        for l in f:
            grid.append([c for c in l.strip()])
    return grid


def number_sides(region_coords: set[Tuple[int, int]]) -> int:
    perimeter = set()
    sides = []
    sorted_coords = sorted(list(region_coords), key=itemgetter(0, 1))
    # print(sorted_coords)
    for r, c in sorted_coords:
        if (r + 1, c) not in region_coords:
            if (
                (r + 1, c - 1, "N") not in perimeter
                and (r + 1, c + 1, "N") not in perimeter
                and (r + 1, c, "N") not in perimeter
            ):
                sides.append((r + 1, c))
            perimeter.add((r + 1, c, "N"))

        if (r - 1, c) not in region_coords:
            if (
                (r - 1, c - 1, "S") not in perimeter
                and (r - 1, c + 1, "S") not in perimeter
                and (r - 1, c, "S") not in perimeter
            ):
                sides.append((r - 1, c))
            perimeter.add((r - 1, c, "S"))

        if (r, c + 1) not in region_coords:
            if (
                (r - 1, c + 1, "E") not in perimeter
                and (r + 1, c + 1, "E") not in perimeter
                and (r, c + 1, "E") not in perimeter
            ):
                sides.append((r, c + 1))
            perimeter.add((r, c + 1, "E"))

        if (r, c - 1) not in region_coords:
            if (
                (r - 1, c - 1, "W") not in perimeter
                and (r + 1, c - 1, "W") not in perimeter
                and (r, c - 1, "W") not in perimeter
            ):
                sides.append((r, c - 1))
            perimeter.add((r, c - 1, "W"))

    # print(len(perimeter), sides, len(sides))
    return len(sides)


def get_neighbours(grid, r, c, n_rows, n_cols):
    next_visit = set()
    grid_value = grid[r][c]
    next_locs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    for nr, nc in next_locs:
        if nr < 0 or nr >= n_rows or nc < 0 or nc >= n_cols:
            continue

        if grid[nr][nc] == grid_value:
            next_visit.add((nr, nc))
    return next_visit


def find_region(grid: list[list[str]], r: int, c: int) -> set[Tuple[int, int]]:

    nrows = len(grid)
    ncols = len(grid[0])
    visited = set([(r, c)])
    next = get_neighbours(grid, r, c, nrows, ncols)
    while next:
        new = set()
        for nr, nc in next:
            visited.add((nr, nc))
            for new_r, new_c in get_neighbours(grid, nr, nc, nrows, ncols):
                if (new_r, new_c) not in visited:
                    new.add((new_r, new_c))

        next = new

    return visited


def find_perimeter(region_coords: set[Tuple[int, int]]) -> int:
    perimeter = 0
    for r, c in region_coords:
        if (r + 1, c) not in region_coords:
            perimeter += 1

        if (r - 1, c) not in region_coords:
            perimeter += 1

        if (r, c + 1) not in region_coords:
            perimeter += 1

        if (r, c - 1) not in region_coords:
            perimeter += 1

    return perimeter


def p1(input: str):
    total_cost = 0
    total_discounted = 0
    visited_regions = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            c = input[i][j]
            # if count_areas[c] > 0:
            if (i, j) in visited_regions:
                continue

            region_coords = find_region(input, i, j)
            visited_regions = visited_regions.union(region_coords)
            area = len(region_coords)
            # count_areas[c] -= area
            perimeter = find_perimeter(region_coords)
            sides = number_sides(region_coords)
            cost = area * perimeter
            discounted = area * sides
            total_cost += cost
            total_discounted += discounted
            # print(c, (i, j), area, perimeter, sides, cost, discounted)

    return total_cost, total_discounted


if __name__ == "__main__":

    sample = "AAAA\nBBCD\nBBCC\nEEEC"
    sample = [[c for c in s] for s in sample.split("\n")]
    sample_2 = "RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE"
    sample_2 = [[c for c in s] for s in sample_2.split("\n")]
    sample_3 = "EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE"
    sample_3 = [[c for c in s] for s in sample_3.split("\n")]
    sample_4 = "AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA"
    sample_4 = [[c for c in s] for s in sample_4.split("\n")]
    grid = load_grid("./2024/d12.txt")

    print(p1(sample))
    print(p1(sample_2))
    print(p1(sample_3))
    print(p1(sample_4))
    print(p1(grid))
