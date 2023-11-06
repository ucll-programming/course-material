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



class Unit:
    def __init__(self, health, firepower, armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError()
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor

    @property
    def health(self):
        return self.__health

    @property
    def firepower(self):
        return self.__firepower

    @property
    def armor(self):
        return self.__armor

    def shot_by(self, other):
        health_loss = max(0, other.firepower - self.armor)
        self.__health = max(0, self.__health - health_loss)


class Tweet:
    def __init__(self, message, max_length):
        self.__message = message  # Cannot call message setter, as it requires max_length to be initialized
        self.max_length = max_length

    def __truncate(self):
        self.__message = self.__message[:self.__max_length]

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message
        self.__truncate()

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, max_length):
        if max_length < 1:
            raise ValueError()
        self.__max_length = max_length
        self.__truncate()
