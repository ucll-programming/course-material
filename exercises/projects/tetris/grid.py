class Grid:
    def __init__(self, width, height, value):
        self.__grid = [
            [value] * width
            for _ in range(height)
        ]

    @property
    def width(self):
        return len(self.__grid[0])

    @property
    def height(self):
        return len(self.__grid)


    def size(self):
        return (self.width, self.height)


    def column(self, index):
        return [row[index] for row in self.__grid]


    def transpose(self):
        return [self.column(index) for index in range(self.width)]


    def rotate_cw(self):
        return self.transpose(list(reversed(self.__grid)))


    def rotate_ccw(self):
        return self.rotate_cw().rotate_cw().rotate_cw()


    def copy(self):
        return [row[:] for row in self.__grid]
