from position import Position


class Grid:
    def __init__(self, width, height, value):
        self.__grid = [
            [value] * width
            for _ in range(height)
        ]

    @staticmethod
    def from_lists(xss):
        width = len(xss[0])
        height = len(xss)
        grid = Grid(width, height, None)
        for y in range(height):
            for x in range(width):
                grid[Position(x, y)] = xss[y][x]
        return grid

    @property
    def width(self):
        return len(self.__grid[0])

    @property
    def height(self):
        return len(self.__grid)

    @property
    def size(self):
        return (self.width, self.height)

    def column(self, index):
        return [row[index] for row in self.__grid]

    def row(self, index):
        return self.__grid[index][:]

    def rotate_ccw(self):
        return Grid.from_lists([list(reversed(self.column(index))) for index in range(self.width)])

    def rotate_cw(self):
        return self.rotate_ccw().rotate_ccw().rotate_ccw()

    def copy(self):
        return Grid.from_lists([row[:] for row in self.__grid])

    def __getitem__(self, position):
        return self.__grid[position.y][position.x]

    def __setitem__(self, position, value):
        self.__grid[position.y][position.x] = value

    def inside(self, position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height
