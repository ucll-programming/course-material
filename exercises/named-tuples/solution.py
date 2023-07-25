from collections import namedtuple


Color = namedtuple('Color', ['r', 'g', 'b'])


def valid_color(color):
    def valid(x):
        return 0 <= x <= 255

    return valid(color.r) and valid(color.g) and valid(color.b)
