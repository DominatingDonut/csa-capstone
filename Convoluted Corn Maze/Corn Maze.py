from random import randint


def build_maze(m, n, swag):
    m -= 1
    n -= 1
    grid = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append("wall")
        grid.append(row)
    start_i = randint(0, m)
    start_j = randint(0, n)
    grid[start_i][start_j] = "start"
    mow(grid, m, n)
    explore_maze(grid, start_i, start_j, swag)
    return grid


def print_maze(grid):
    for row in grid:
        printable_row = ""
        for cell in row:
            if cell == "wall":
                char = '|'
            elif cell == "empty":
                char = ' '
            elif cell == "start":
                char = 'X'
            elif cell == "end":
                char = 'O'
            else:
                char = cell[0]
            printable_row += char
        print(printable_row)


def mow(grid, i, j):
    directions = ['U', 'D', 'L', 'R']
    while directions:
        directions_index = randint(0, len(directions) - 1)
        direction = directions.pop(directions_index)
        if direction == 'U':
            if i < 2:
                continue
            elif grid[i - 2][j] == 'wall':
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j)
        elif direction == 'D':
            if i + 2 >= len(grid):
                continue
            elif grid[i + 2][j] == 'wall':
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j)
        elif direction == 'L':
            if j < 2:
                continue
            elif grid[i][j - 2] == 'wall':
                grid[i][j - 1] = 'empty'
                grid[i][j - 2] = 'empty'
                mow(grid, i, j - 2)
        else:
            if j + 2 >= len(grid[0]):
                continue
            elif grid[i][j + 2] == 'wall':
                grid[i][j + 1] = 'empty'
                grid[i][j + 2] = 'empty'
                mow(grid, i, j + 2)


def explore_maze(grid, start_i, start_j, swag):
    grid_copy = [row[:] for row in grid]
    bfs_queue = [[start_i, start_j]]
    directions = ['U', 'D', 'L', 'R']
    while bfs_queue:
        i, j = bfs_queue.pop(0)
        if grid[i][j] != "start":
            grid_copy[i][j] = 'visited'
            if randint(1, 10) == 1:
                grid[i][j] = swag[randint(0, len(swag) - 1)]

        for direction in directions:
            explore_i, explore_j = i, j

            if direction == 'U':
                explore_i = i - 1
            elif direction == 'D':
                explore_i = i + 1
            elif direction == 'L':
                explore_j = j - 1
            else:
                explore_j = j + 1

            if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
                continue

            if grid_copy[explore_i][explore_j] != "wall" and grid_copy[explore_i][explore_j] != "visited":
                bfs_queue.append([explore_i, explore_j])
    grid[i][j] = 'end'


print_maze(build_maze(15, 25, ['candy corn', 'werewolf', 'pumpkin']))