import pytest
import student


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


nocturnal_animals = cm(
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

billboards = cm(
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

fargo = cm(
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

magnolia = cm(
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

west = cm(
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

america = cm(
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

casino = cm(
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

stardust = cm(
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

goodfellas = cm(
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


def test_movie_exists():
    assert 'Movie' in dir(student)


@if_defined('Movie', 'actor_count')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("movie, expected", [
    (goodfellas, 4),
    (stardust, 6),
    (casino, 5),
    (magnolia, 8),
])
def test_actor_count(movie, expected):
    actual = student.actor_count(movie)
    assert expected == actual
