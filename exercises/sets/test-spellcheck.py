import pytest
import student
import itertools
from string import ascii_lowercase


@pytest.mark.timeout(1)
@pytest.mark.parametrize("document, valid_words, expected", [
    (
        "",
        [],
        set()
    ),
    (
        "word",
        ['word'],
        set()
    ),
    (
        "wort",
        ['word'],
        {'wort'}
    ),
    (
        "Word",
        ['word'],
        set()
    ),
    (
        "Word word WORD worD",
        ['word'],
        set()
    ),
    (
        "WORT",
        ['word'],
        {'wort'}
    ),
    (
        "the cat\nsat on\nthe mat",
        ['cat', 'sat', 'mat'],
        {'the', 'on'}
    ),
])
def test_spellcheck(document, valid_words, expected):
    actual = student.spellcheck(document, valid_words)
    assert expected == actual


@pytest.mark.timeout(1)
def test_spellcheck_large_input():
    valid_words = [
        "".join(word)
        for i in range(2, 5)
        for word in itertools.combinations(ascii_lowercase, i)
    ]
    invalid_words = ["".join(word) for word in itertools.combinations(ascii_lowercase, 6)]
    document = "\n".join([
        f'{valid} {invalid}' for valid, invalid in zip(valid_words, invalid_words)
    ]) + "\n" + " ".join(invalid_words)
    expected = set(invalid_words)
    actual = student.spellcheck(document, valid_words)
    assert expected == actual
