from collections import namedtuple
from operator import attrgetter


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


Movie = namedtuple('Movie', ['title', 'runtime', 'director', 'actors'])


def actor_count(movie):
    return len(movie.actors)


def movies_by(movies, director):
    return [
        movie.title
        for movie in movies
        if movie.director == director
    ]


def longest_movie(movies):
    return max(movies, key=attrgetter('runtime'))
