def width(grid):
    return len(grid[0])


def height(grid):
    return len(grid)


def column(grid, index):
    return [row[index] for row in grid]


def transpose(grid):
    return [column(grid, index) for index in range(width(grid))]


def rotate_cw(grid):
    return transpose(list(reversed(grid)))


def rotate_ccw(grid):
    return rotate_cw(rotate_cw(rotate_cw(grid)))


def copy(grid):
    return [row[:] for row in grid]
