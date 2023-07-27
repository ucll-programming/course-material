class Pair:
    def __init__(self):
        self.first = None
        self.second = None


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        return self.lower > self.upper

    def contains(self, value):
        return self.lower <= value <= self.upper

    def overlaps_with(self, other):
        if self.is_empty() or other.is_empty():
            return False
        return self.contains(other.lower) or self.contains(other.upper) or other.contains(self.lower)


class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, string):
        return self.__password == string


class Averager:
    def __init__(self):
        self.reset()

    def reset(self):
        self.__sum = 0
        self.__count = 0

    def add(self, value):
        self.__sum += value
        self.__count += 1

    def average(self):
        return self.__sum / self.__count


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
