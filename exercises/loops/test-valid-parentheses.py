import functools
import itertools
import pytest
import student


@functools.cache
def generate_valid_strings_of_length(n):
    if n == 0:
        return ('',)
    else:
        return tuple((
            f"({r1}){r2}"
            for k in range(1, n + 1)
            for r1 in generate_valid_strings_of_length(k - 1)
            for r2 in generate_valid_strings_of_length(n - k)
        ))


def generate_valid_strings_of_length_up_to(n):
    for k in range(n + 1):
        yield from generate_valid_strings_of_length(k)


@functools.cache
def generate_strings_of_length(n):
    if n == 0:
        return ("",)
    else:
        return tuple((
            f'{x}{y}'
            for x in '()'
            for y in generate_strings_of_length(n - 1)
        ))


def generate_invalid_strings_of_length(n):
    valid = set(generate_valid_strings_of_length(n))
    for string in generate_strings_of_length(2 * n):
        if string not in valid:
            yield string


def generate_invalid_strings_of_length_up_to(n):
    for k in range(n + 1):
        yield from generate_invalid_strings_of_length(k)


@pytest.mark.parametrize("string", generate_valid_strings_of_length_up_to(8))
def test_valid_parentheses(string):
    actual = student.valid_parentheses(string)

    assert actual == True, f"valid_parentheses({string!r}) should return True"


@pytest.mark.parametrize("string", itertools.chain(
    generate_invalid_strings_of_length_up_to(5),
    itertools.islice(generate_invalid_strings_of_length(8), 100)
))
def test_not_valid_parentheses(string):
    actual = student.valid_parentheses(string)

    assert actual == False, f"valid_parentheses({string!r}) should return False"
