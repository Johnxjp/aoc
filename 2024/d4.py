def load(filename: str):
    grid = []
    with open(filename) as f:
        for line in f:
            row = [c for c in line.strip()]
            grid.append(row)
    return grid


def search(grid, keyword, start_x, start_y, height, width) -> int:
    """
    Returns the number of times the keyword appears in the grid
    when searching from the start position vertically, horizontally, diagonally
    """

    if grid[start_x][start_y] != keyword[0]:
        return 0

    matches = 0
    # Search Horizontal forward
    if start_y + (len(keyword) - 1) < width:
        word = "".join(grid[start_x][start_y : start_y + len(keyword)])
        matches += word == keyword
        if word == keyword:
            print("Matched horizontal forward starting", start_x, start_y)

    # Search Horizontal backward
    if start_y - (len(keyword) - 1) >= 0:
        word = "".join(
            grid[start_x][start_y - (len(keyword) - 1) : start_y + 1][::-1]
        )
        matches += word == keyword
        if word == keyword:
            print("Matched horizontal backward starting", start_x, start_y)

    # Search Vertical upward
    if start_x - (len(keyword) - 1) >= 0:
        word = "".join(
            [grid[start_x - i][start_y] for i in range(len(keyword))]
        )
        matches += word == keyword
        if word == keyword:
            print("Matched vertical up starting", start_x, start_y)

    # Search Vertical down
    if start_x + (len(keyword) - 1) < height:
        word = "".join(
            [grid[start_x + i][start_y] for i in range(len(keyword))]
        )
        matches += word == keyword
        if word == keyword:
            print("Matched vertical down starting", start_x, start_y)

    # Search diag centre-TL
    for i in range(len(keyword)):
        curr_x, curr_y = start_x - i, start_y - i
        if curr_x < 0 or curr_y < 0 or grid[curr_x][curr_y] != keyword[i]:
            break

    else:
        print("Matched centre-TL starting", start_x, start_y)
        matches += 1

    # Search diag centre-BR
    for i in range(len(keyword)):
        curr_x, curr_y = start_x + i, start_y + i
        if (
            curr_x >= height
            or curr_y >= width
            or grid[curr_x][curr_y] != keyword[i]
        ):
            break

    else:
        print("Matched centre-BR starting", start_x, start_y)
        matches += 1

    # Search diag centre-BL
    for i in range(len(keyword)):
        curr_x, curr_y = start_x + i, start_y - i
        if (
            curr_x >= height
            or curr_y < 0
            or grid[curr_x][curr_y] != keyword[i]
        ):
            break

    else:
        print("Matched centre-BL starting", start_x, start_y)
        matches += 1

    # search diag centre-TR
    for i in range(len(keyword)):
        curr_x, curr_y = start_x - i, start_y + i
        if curr_x < 0 or curr_y >= width or grid[curr_x][curr_y] != keyword[i]:
            break

    else:
        print("Matched centre-TR starting", start_x, start_y)
        matches += 1

    return matches


def search_2(grid, keyword, start_x, start_y, height, width) -> int:
    """
    Returns the number of times the keyword appears in the grid
    when searching from the start position vertically, horizontally, diagonally
    """

    if grid[start_x][start_y] != "A":
        return 0

    # TL-BR
    word = ""
    for i in range(-1, 2):
        curr_x, curr_y = start_x + i, start_y + i
        if curr_x < 0 or curr_x >= height or curr_y < 0 or curr_y >= width:
            return 0

        word += grid[curr_x][curr_y]

    if not (word == keyword or word[::-1] == keyword):
        return 0

    # BL-TR
    word = ""
    for i in range(-1, 2):
        curr_x, curr_y = start_x - i, start_y + i
        if curr_x < 0 or curr_x >= height or curr_y < 0 or curr_y >= width:
            return 0

        word += grid[curr_x][curr_y]

    if not (word == keyword or word[::-1] == keyword):
        return 0

    print("Found X-MAS at", start_x, start_y)
    return 1


def d1():
    grid = load("d4.txt")
    height = len(grid)
    width = len(grid[0])
    keyword = "XMAS"
    total_matched = 0
    for r in range(height):
        for c in range(width):
            total_matched += search(grid, keyword, r, c, height, width)

    print(total_matched)


def d2():
    grid = load("d4.txt")
    height = len(grid)
    width = len(grid[0])
    keyword = "MAS"
    total_matched = 0
    for r in range(height):
        for c in range(width):
            total_matched += search_2(grid, keyword, r, c, height, width)

    print(total_matched)


if __name__ == "__main__":
    d1()
    d2()
