from collections import namedtuple


Color = namedtuple('Color', ['r', 'g', 'b'])


def valid_color(color):
    def valid(x):
        return 0 <= x <= 255

    return valid(color.r) and valid(color.g) and valid(color.b)


def clamp_color(color):
    def clamp(x):
        if x < 0:
            return 0
        elif x > 255:
            return 255
        else:
            return x

    return Color(
        clamp(color.r),
        clamp(color.g),
        clamp(color.b),
    )
