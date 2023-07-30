from grid import Grid
from position import Position
import random


class Shape:
    def __init__(self, grid):
        self.__grid = grid

    @property
    def width(self):
        return self.__grid.width

    @property
    def height(self):
        return self.__grid.height

    @property
    def size(self):
        return self.__grid.size

    def rotate_cw(self):
        return Shape(self.__grid.rotate_cw())

    def rotate_ccw(self):
        return Shape(self.__grid.rotate_ccw())

    def __getitem__(self, position):
        return self.__grid[position]


def _parse_shape(string, color):
    lines = [line.strip() for line in string.strip().splitlines()]
    width = len(lines[0])
    height = len(lines)
    grid = Grid(width, height, None)

    for x in range(width):
        for y in range(height):
            if lines[y][x] == 'x':
                grid[Position(x, y)] = color

    return Shape(grid)



def shape_O(color):
    return _parse_shape('''
        xx
        xx
        ''', color)

def shape_S(color):
    return _parse_shape('''
        .xx
        xx.
        ''', color)

def shape_Z(color):
    return _parse_shape('''
        xx.
        .xx
        ''', color)

def shape_I(color):
    return _parse_shape('''
        xxxx
        ''', color)

def shape_L(color):
    return _parse_shape('''
        xxx
        x..
        ''', color)

def shape_J(color):
    return _parse_shape('''
        x..
        xxx
        ''', color)

def shape_T(color):
    return _parse_shape('''
        .x.
        xxx
        ''', color)

def random_shape():
    color = random.randint(0, 2)
    return random.choice([
        shape_I,
        shape_J,
        shape_L,
        shape_O,
        shape_S,
        shape_T,
        shape_Z,
    ])(color)
