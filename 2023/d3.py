from collections import defaultdict


def read_lines():
    with open("2023/d3.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    return lines


def get_coords_to_check(row_id, min_col_id, max_col_id, max_row, max_col):
    coords = []
    for r in range(max(0, row_id - 1), min(row_id + 2, max_row)):
        for c in range(max(0, min_col_id - 1), min(max_col_id + 2, max_col)):
            coords.append((r, c))
    return coords


def parse_graph(lines):
    sum_part_numbers = 0
    max_row, max_col = len(lines), len(lines[0])
    for row_id, row in enumerate(lines):
        col_id = 0
        while col_id < max_col:
            part_number = 0
            part_index = 0

            # Get the Number
            while col_id < max_col and row[col_id].isdigit():
                col = row[col_id]
                part_number = part_number * 10 + int(col)
                part_index += 1
                col_id += 1

            # Check if there is a symbol adjacent
            if part_number:
                print(part_number, part_index, col, col_id)
                max_col_id = col_id - 1
                min_col_id = col_id - part_index
                coords_to_check = get_coords_to_check(
                    row_id, min_col_id, max_col_id, max_row, max_col
                )
                for r, c in coords_to_check:
                    if lines[r][c] != "." and not lines[r][c].isdigit():
                        sum_part_numbers += part_number
                        break

            # But jumping twice now!
            col_id += 1

    return sum_part_numbers


def p1():
    lines = read_lines()
    print(parse_graph(lines))


def gear_ratio(lines):
    max_row, max_col = len(lines), len(lines[0])
    gear_coords = defaultdict(list)
    for row_id, row in enumerate(lines):
        col_id = 0
        while col_id < max_col:
            part_number = 0
            part_index = 0

            # Get the Number
            while col_id < max_col and row[col_id].isdigit():
                col = row[col_id]
                part_number = part_number * 10 + int(col)
                part_index += 1
                col_id += 1

            # Check if there is a symbol adjacent
            if part_number:
                print(part_number, part_index, col, col_id)
                max_col_id = col_id - 1
                min_col_id = col_id - part_index
                coords_to_check = get_coords_to_check(
                    row_id, min_col_id, max_col_id, max_row, max_col
                )
                for r, c in coords_to_check:
                    if lines[r][c] == "*":
                        gear_coords[(r, c)].append(part_number)

            # But jumping twice now!
            col_id += 1

    sum_gear_ratios = 0
    for gears_coords, parts in gear_coords.items():
        if len(parts) == 2:
            sum_gear_ratios += parts[0] * parts[1]

    return sum_gear_ratios


def p2():
    lines = read_lines()
    print(gear_ratio(lines))


if __name__ == "__main__":
    p1()
    p2()
