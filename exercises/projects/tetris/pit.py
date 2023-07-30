from position import Position
from grid import Grid


class Pit:
    def __init__(self, width, height):
        self.__grid = Grid(width, height, None)

    @property
    def width(self):
        return self.__grid.width

    @property
    def height(self):
        return self.__grid.height

    @property
    def size(self):
        return self.__grid.size

    def __getitem__(self, position):
        return self.__grid[position]

    def fits(self, shape, position):
        for dx in range(shape.width):
            for dy in range(shape.height):
                block_position_in_shape = Position(dx, dy)
                block_position_in_pit = position + block_position_in_shape
                if not self.__grid.inside(block_position_in_pit):
                    return False
                if self[block_position_in_pit] is not None and shape[block_position_in_shape] is not None:
                    return False
        return True

    def place_shape(self, shape, position):
        for dx in range(shape.width):
            for dy in range(shape.height):
                delta = Position(dx, dy)
                if shape[delta] is not None:
                    self.__grid[position + delta] = shape[delta]

    def drop_shape(self, shape, position):
        while self.fits(shape, next_position := position + Position(0, 1)):
            position = next_position
        self.place_shape(shape, position)

    def __is_row_full(self, row_index):
        return all(block is not None for block in self.__grid.row(row_index))

    def __copy_row(self, origin, target):
        for x in range(self.width):
            self.__grid[Position(x, target)] = self.__grid[Position(x, origin)]

    def __empty_row(self, y):
        for x in range(self.width):
            self.__grid[Position(x, y)] = None

    def remove_full_rows(self):
        i = j = self.height - 1
        while j >= 0:
            while j >= 0 and self.__is_row_full(j):
                j -= 1
            if i != j:
                self.__copy_row(j, i)
                j -= 1
            i -= 1
            j = min(i, j)

        while i >= 0:
            self.__empty_row(i)
            i -= 1
