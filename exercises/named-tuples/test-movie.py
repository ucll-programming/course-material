import pytest
import student
from functools import cache


def is_defined(function_name):
    return function_name in dir(student)


def if_defined(*identifiers):
    condition = all(is_defined(identifier) for identifier in identifiers)
    return pytest.mark.skipif(not condition, reason=f'One of {identifiers!r} not found in student module')


def test_movie_exists():
    assert 'Movie' in dir(student)


def cm(**kwargs):
    if 'Movie' in dir(student):
        return student.Movie(**kwargs)
    else:
        return None


@cache
def nocturnal_animals():
    return cm(
        title='Nocturnal Animals',
        runtime=116,
        director='Tom Ford',
        actors=(
            'Amy Adams',
            'Jake Gyllenhaal',
            'Michael Shannon',
            'Aaron Taylor-Johnson',
            'Isla Fisher',
        )
    )

@cache
def billboards():
    return cm(
        title='Three Billboards Outside Ebbing, Missouri',
        runtime=115,
        director='Martin McDonagh',
        actors=(
            'Frances McDormand',
            'Woody Harrelson',
            'Sam Rockwell',
            'Peter Dinklage'
        )
    )

@cache
def fargo():
    return cm(
        title='Fargo',
        runtime=98,
        director='Coen Brothers',
        actors=(
            'William H. Macy',
            'Frances McDormand',
            'Steve Buscemi',
            'Peter Stormare'
        )
    )

@cache
def magnolia():
    return cm(
        title='Magnolia',
        runtime=188,
        director='Paul Thomas Anderson',
        actors=(
            'Tom Cruise',
            'Jason Robards',
            'Julianne Moore',
            'Philip Seymour Hoffman',
            'Philip Baker Hall',
            'William H. Hacy',
            'Alfred Molina',
            'John C. Reilly'
        )
    )

@cache
def west():
    return cm(
        title='Once Upon a Time in the West',
        runtime=165,
        director='Sergio Leone',
        actors=(
            'Henry Fonda',
            'Charles Bronson',
            'Claudia Cardinale',
            'Jason Robards',
        )
    )

@cache
def america():
    return cm(
        title='Once Upon a Time in America',
        runtime=229,
        director='Sergio Leone',
        actors=(
            'Robert De Niro',
            'James Woods',
            'Joe Pesci',
            'Jennifer Connelly',
        )
    )

@cache
def casino():
    return cm(
        title='Casino',
        runtime=178,
        director='Martin Scorsese',
        actors=(
            'Robert De Niro',
            'Joe Pesci',
            'James Woods',
            'Sharon Stone',
            'Kevin Pollack',
        ),
    )

@cache
def stardust():
    return cm(
        title='Stardust',
        runtime=127,
        director='Matthew Vaugh',
        actors=(
            'Charlie Cox',
            'Claire Danes',
            'Robert De Niro',
            'Henry Cavill',
            "Peter O'Toole",
            'Mark Strong',
        )
    )

@cache
def goodfellas():
    return cm(
        title='Goodfellas',
        runtime=145,
        director='Marin Scorsese',
        actors=(
            'Robert De Niro',
            'Ray Liotta',
            'Hoe Pesci',
            'Lorraine Bracco',
        )
    )

@cache
def gbu():
    return cm(
        title='The Good, the Bad and the Ugly',
        runtime=148,
        director='Sergio Leone',
        actors=(
            'Clint Eastwood',
            'Lee Van Cleef',
            'Eli Wallach',
        )
    )

@cache
def fury_road():
    return cm(
        title='Mad Max: Fury Road',
        runtime=120,
        director='George Miller',
        actors=(
            'Tom Hardy',
            'Charlize Theron',
            'Nicholas Hoult',
        )
    )


@pytest.fixture
def movies():
    return [
        nocturnal_animals(),
        billboards(),
        fargo(),
        magnolia(),
        west(),
        america(),
        casino(),
        stardust(),
        goodfellas(),
        gbu(),
        fury_road(),
    ]


def test_movie_exists():
    assert 'Movie' in dir(student)


def test_movie():
    movie = fury_road()
    assert movie.title == 'Mad Max: Fury Road'
    assert movie.runtime == 120
    assert movie.director == 'George Miller'
    assert movie.actors == ('Tom Hardy', 'Charlize Theron', 'Nicholas Hoult')


@if_defined('Movie', 'actor_count')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("movie, expected", [
    (goodfellas(), 4),
    (stardust(), 6),
    (casino(), 5),
    (magnolia(), 8),
])
def test_actor_count(movie, expected):
    actual = student.actor_count(movie)
    assert expected == actual


@if_defined('Movie', 'movies_by')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("director, expected", [
    (
        'Paul Thomas Anderson',
        [
            'Magnolia',
        ]
    ),
    (
        'Sergio Leone',
        [
            'The Good, the Bad and the Ugly',
            'Once Upon a Time in America',
            'Once Upon a Time in the West',
        ]
    ),
    (
        'Darren Aronosky',
        []
    )
])
def test_movies_by(movies, director, expected):
    actual = student.movies_by(movies, director)
    assert len(expected) == len(actual)
    assert set(expected) == set(actual)


@if_defined('Movie', 'longest_movie')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("movies, expected", [
    (
        [west()],
        west()
    ),
    (
        [west(), america()],
        america(),
    ),
    (
        [america(), west()],
        america(),
    ),
    (
        [casino(), goodfellas(), stardust(), gbu()],
        casino(),
    ),
    (
        [goodfellas(), casino(), stardust(), gbu()],
        casino(),
    ),
    (
        [goodfellas(), stardust(), casino(), gbu()],
        casino(),
    ),
    (
        [goodfellas(), stardust(), gbu(), casino()],
        casino(),
    ),
])
def test_longest_movie(movies, expected):
    actual = student.longest_movie(movies)
    assert expected is actual
