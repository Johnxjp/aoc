import sys
from typing import Set, Tuple


def find_starting_position(grid: list[str]) -> Tuple[int, int, int, int]:
    """Find the guard's starting position and orientation."""
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in directions:
                dy, dx = directions[grid[row][col]]
                return row, col, dy, dx
    
    raise ValueError("No guard found in grid")


def turn_right(dy: int, dx: int) -> Tuple[int, int]:
    """Turn right 90 degrees."""
    # North -> East: (-1, 0) -> (0, 1)
    # East -> South: (0, 1) -> (1, 0)
    # South -> West: (1, 0) -> (0, -1)
    # West -> North: (0, -1) -> (-1, 0)
    return dx, -dy


def simulate_path(grid: list[str], start_row: int, start_col: int, 
                  start_dy: int, start_dx: int, 
                  obstacle_row: int = -1, obstacle_col: int = -1) -> Tuple[bool, Set[Tuple[int, int]]]:
    """
    Simulate the guard's path. 
    Returns (True, visited_positions) if guard escapes, (False, visited_positions) if guard loops.
    If obstacle_row and obstacle_col are provided, temporarily place an obstacle there.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    row, col = start_row, start_col
    dy, dx = start_dy, start_dx
    
    # Track visited states (position + direction) to detect loops
    visited_states = set()
    visited_positions = set()
    
    while True:
        # Check if we've been in this exact state before (loop detection)
        state = (row, col, dy, dx)
        if state in visited_states:
            return False, visited_positions  # Found a loop!
        
        visited_states.add(state)
        visited_positions.add((row, col))
        
        # Calculate next position
        next_row = row + dy
        next_col = col + dx
        
        # Check if next position is out of bounds (guard escapes)
        if next_row < 0 or next_row >= n_rows or next_col < 0 or next_col >= n_cols:
            return True, visited_positions  # Guard escaped
        
        # Check if next position has an obstacle (including temporary one)
        is_obstacle = grid[next_row][next_col] == '#'
        if obstacle_row == next_row and obstacle_col == next_col:
            is_obstacle = True
        
        if is_obstacle:
            # Turn right but stay in same position
            dy, dx = turn_right(dy, dx)
        else:
            # Move forward
            row, col = next_row, next_col


def find_loop_positions(grid: list[str]) -> int:
    """Find all positions where placing an obstacle would create a loop."""
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    # Find starting position
    start_row, start_col, start_dy, start_dx = find_starting_position(grid)
    
    # First, get the guard's original path (without any new obstacles)
    escaped, original_path = simulate_path(grid, start_row, start_col, start_dy, start_dx)
    
    if not escaped:
        print("Guard is already in a loop!")
        return 0
    
    # Try placing an obstacle at each position on the original path
    # (except the starting position)
    loop_positions = set()
    
    for obstacle_row, obstacle_col in original_path:
        # Can't place obstacle at starting position or on existing obstacles
        if (obstacle_row == start_row and obstacle_col == start_col) or \
           grid[obstacle_row][obstacle_col] == '#':
            continue
        
        # Simulate with this obstacle
        escaped, _ = simulate_path(grid, start_row, start_col, start_dy, start_dx,
                                   obstacle_row, obstacle_col)
        
        if not escaped:
            loop_positions.add((obstacle_row, obstacle_col))
    
    return len(loop_positions)


def solve_part1(grid: list[str]) -> int:
    """Solve part 1: count unique positions visited."""
    start_row, start_col, start_dy, start_dx = find_starting_position(grid)
    escaped, visited = simulate_path(grid, start_row, start_col, start_dy, start_dx)
    return len(visited)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python guard_patrol_fixed.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        grid = [line.strip() for line in f]
    
    # Part 1
    part1_answer = solve_part1(grid)
    print(f"Part 1 - Unique positions visited: {part1_answer}")
    
    # Part 2
    part2_answer = find_loop_positions(grid)
    print(f"Part 2 - Positions that create loops: {part2_answer}")