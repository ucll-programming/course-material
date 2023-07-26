class Pair:
    def __init__(self):
        self.first = None
        self.second = None


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Counter:
    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1

    def reset(self):
        self.__count = 0
