import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('d1, d2, expected', [
    (
        {},
        {},
        {}
    ),
    (
        {'dog': 'hond'},
        {},
        {}
    ),
    (
        {'dog': 'hond'},
        {'hond': 'chien'},
        {'dog': 'chien'}
    ),
    (
        {'dog': 'hond', 'cat': 'kat'},
        {'hond': 'chien'},
        {'dog': 'chien'}
    ),
    (
        {'dog': 'hond', 'cat': 'kat'},
        {'hond': 'chien', 'kat': 'chat'},
        {'dog': 'chien', 'cat': 'chat'}
    ),
    (
        {'dog': 'hond', 'cat': 'kat', 'elephant': 'olifant'},
        {'hond': 'chien', 'kat': 'chat'},
        {'dog': 'chien', 'cat': 'chat'}
    ),
    (
        {'dog': 'hond', 'cat': 'kat', 'elephant': 'olifant'},
        {'hond': 'chien', 'kat': 'chat', 'zeehond': 'phoque'},
        {'dog': 'chien', 'cat': 'chat'}
    ),
    (
        {'dog': 'hond', 'cat': 'kat', 'elephant': 'olifant', 'seal': 'zeehond'},
        {'hond': 'chien', 'kat': 'chat', 'zeehond': 'phoque'},
        {'dog': 'chien', 'cat': 'chat', 'seal': 'phoque'}
    ),
])
def test_combine(d1, d2, expected):
    actual = student.combine(d1, d2)
    assert expected == actual
