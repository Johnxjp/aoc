"""  
Ideal algorithm is BFS from each starting 0. Save set of
9s visited so don't double count

Possible to also DFS from all 0s. Keep track of visited to cut short.
Stop when no more neighbours

Probably optimisations
"""

def load_grid(filename: str) -> list[list[int]]:
    grid = []
    with open(filename) as f:
        for line in f:
            row = [int(c) for c in line.strip()]
            grid.append(row)
    return grid

def get_neighbours(grid, r, c, n_rows, n_cols):
    next_visit = set()
    grid_value = grid[r][c]
    next_locs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    for nr, nc in next_locs:
        if nr < 0 or nr >= n_rows or nc < 0 or nc >= n_cols:
            continue
        
        if grid[nr][nc] - grid_value == 1:
            next_visit.add((nr, nc))
    return next_visit

def bfs(grid: list[list[int]], target_value: int, r: int, c: int) -> int:
    n_rows = len(grid)
    n_cols = len(grid[0])
    score = 0
    visited = set()
    next_visit = get_neighbours(grid, r, c, n_rows, n_cols)
    while next_visit:
        new_visit = set()
        for nr, nc in next_visit:
            if (nr, nc) in visited:
                continue
            
            visited.add((nr, nc))

            # Don't add more neighbours. Only count 1 unique value
            if grid[nr][nc] == target_value:
                score += 1
            else:
                new_visit = new_visit.union(get_neighbours(grid, nr, nc, n_rows, n_cols))
        
        next_visit = new_visit

    return score

def p1(filename: str, trailhead_ids: int = 0, target_value: int = 9):
    grid = load_grid(filename)
    nrows = len(grid)
    ncols = len(grid[0])
    trailhead_scores = []
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == trailhead_ids:
                score = bfs(grid, target_value, r, c)
                trailhead_scores.append(score)
    
    return sum(trailhead_scores)

def bfs_2(grid: list[list[int]], target_value: int, r: int, c: int) -> int:
    n_rows = len(grid)
    n_cols = len(grid[0])
    score = 0
    next_visit = get_neighbours(grid, r, c, n_rows, n_cols)
    while next_visit:
        new_visit = []
        for nr, nc in next_visit:
            if grid[nr][nc] == target_value:
                score += 1
            else:
                new_visit.extend(get_neighbours(grid, nr, nc, n_rows, n_cols))
        
        next_visit = new_visit

    return score

def p2(filename: str, trailhead_ids: int = 0, target_value: int = 9):
    """ BFS no need to cache """
    grid = load_grid(filename)
    nrows = len(grid)
    ncols = len(grid[0])
    trailhead_scores = []
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == trailhead_ids:
                score = bfs_2(grid, target_value, r, c)
                trailhead_scores.append(score)
    
    return sum(trailhead_scores)

if __name__ == "__main__":
    print("Part 1")
    print(p1("./2024/d10-sample.txt"))
    print(p1("./2024/d10-sample-2.txt"))
    print(p1("./2024/d10.txt"))

    print("Part 2")
    print(p2("./2024/d10-sample.txt"))
    print(p2("./2024/d10-sample-2.txt"))
    print(p2("./2024/d10.txt"))
