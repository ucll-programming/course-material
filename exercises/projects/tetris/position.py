class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x + other.y, self.y + other.y)

    def __mul__(self, factor):
        return Position(self.x * factor, self.y * factor)

    def __eq__(self, other):
        if isinstance(other, Position):
            return (self.x, self.y) == (other.x, other.y)
        else:
            return NotImplemented

    def __str__(self):
        return f'({self.x}, {self.y})'