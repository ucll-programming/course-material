import pytest
import student


@pytest.mark.parametrize("name, expected", [
    ("John", "Hello, John!"),
    ("Peter", "Hello, Peter!"),
    ("Anne", "Hello, Anne!"),
    ("Consuela", "Hello, Consuela!"),
])
def test_greet(name, expected):
    actual = student.greet(name)
    assert expected == actual, f'greet({name}) should return {expected!r}'
