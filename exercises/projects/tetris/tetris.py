import grid


def create_pit(width, height):
    return grid.create(width, height, None)


def pit_width(pit):
    return grid.width(pit)


def pit_height(pit):
    return grid.height(pit)


def pit_size(pit):
    return grid.size(pit)


def fits(pit, shape, position):
    pit_width, pit_height = pit_size(pit)
    shape_width, shape_height = grid.size(shape)
    x, y = position
    if x + shape_width >= pit_width:
        return False
    if y + shape_height >= pit_height:
        return False
    for dx in range(shape_width):
        for dy in range(shape_height):
            if pit[y + dy][x + dx] is not None and shape[dy][dx] is not None:
                return False
    return True


def place_shape(pit, shape, position):
    shape_width, shape_height = grid.size(shape)
    x, y = position
    for dx in range(shape_width):
        for dy in range(shape_height):
            if shape[dy][dx] is not None:
                pit[y + dy][x + dx] = shape[dy][dx]


def rotate_shape(shape):
    return grid.rotate_cw(shape)


def drop_shape(pit, shape, position):
    x, y = position
    while fits(pit, shape, (x, y + 1)):
        y += 1
    place_shape(pit, shape, (x, y))


def is_row_full(row):
    return all(block is not None for block in row)


def copy_row(pit, origin, target):
    for x in range(pit_width(pit)):
        pit[target][x] = pit[origin][x]


def empty_row(pit, y):
    for x in range(pit_width(pit)):
        pit[y][x] = None


def remove_full_rows(pit):
    pit_height = pit_height(pit)
    i = j = pit_height - 1
    count = 0
    while j >= 0:
        while j >= 0 and not is_row_full(pit, j):
            j -= 1
            count += 1
        if i != j:
            copy_row(pit, j, i)
            i -= 1
            j -= 1
    while i >= 0:
        empty_row(pit, i)
        i -= 1
    return count
