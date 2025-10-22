"""
How to solve this. We need to track
- the guard's location on the grid
- the direction the guard is facing

Then we keep track of distinct locations visited.

Then we decide next step by assessing if there is an obstacle in the guard's path.
There is a chance that the guard might have to turn multiple times before moving.

The steps are:
1. Try to take a step forward in direction facing.
- If can, do it and record square if unique
- If heading out of bounds, stop
- If obstacle, turn right and try 1. again

We will represent orientation as [x][y]. Essentially increments will take

- North: -1, 0
- South: 1, 0
- West: 0, -1
- East, 0, 1

"""

import sys
from typing import Tuple


def _find_starting_orientation(grid_string: str) -> Tuple[int, int, int]:
    """Find index of guard in 1d-string and orientation"""
    if (index := grid_string.find("^")) >= 0:
        return index, -1, 0

    if (index := grid_string.find(">")) >= 0:
        return index, 0, 1

    if (index := grid_string.find("v")) >= 0:
        return index, 1, 0

    if (index := grid_string.find("<")) >= 0:
        return index, 0, -1


def find_starting_orientation(grid_string: str, n_cols: int) -> Tuple[int, int, int, int]:
    """Searches for guard and starting direction"""
    index, dy, dx = _find_starting_orientation(grid_string)
    row = index // n_cols
    col = index - (row * n_cols)
    return row, col, dy, dx

def get_new_orientation(dy: int, dx: int) -> Tuple[int, int]:
    """ 
    Turn right and new orientation 

    dy = row increment
    dx = column increment
    """

    # North -> East
    if dy == -1 and dx == 0:
        return 0, 1
    
    # East -> South
    if dy == 0 and dx == 1:
        return 1, 0
    
    # South -> West
    if dy == 1 and dx == 0:
        return 0, -1
    
    # West -> North
    return -1, 0


if __name__ == "__main__":
    filename = sys.argv[1]
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(line.strip())

    n_cols = len(grid[0])
    n_rows = len(grid)
    row, col, dy, dx = find_starting_orientation("".join(grid), n_cols)
    
    # Change grid to 2D
    grid = [[s for s in string] for string in grid]
    unique_visited = set()
    while True:
        next_row, next_col = row + dy, col + dx

        if next_row >= n_rows or next_row < 0 or next_col >= n_cols or next_col < 0:
            # Out of bounds. Escaped! Update final loc
            grid[row][col] = "X"
            unique_visited.add((row, col))
            break

        cell_value = grid[next_row][next_col]

        # Can move if no obstacle '#'
        if cell_value == "." or cell_value == "X":
            # Update current location
            grid[row][col] = "X"
            unique_visited.add((row, col))
            row, col = next_row, next_col
        
        else:
            dy, dx = get_new_orientation(dy, dx)

    print(len(unique_visited))
