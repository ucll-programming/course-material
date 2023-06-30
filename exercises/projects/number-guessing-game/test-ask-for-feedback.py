import pytest
from testlib import *
import student


@pytest.mark.parametrize('inputs, expected', [
    (['lower'], -1),
    (['Lower'], -1),
    (['LOWER'], -1),
    (['lOwEr'], -1),
    (['higher'], 1),
    (['Higher'], 1),
    (['HIGHER'], 1),
    (['correct'], 0),
    (['correcT'], 0),
    (['CorRECT'], 0),
    (['cor', 'CORRECT'], 0),
    (['x', 'x', 'x', 'x', 'lower'], -1),
])
def test_ask_for_feedback(fake_input, inputs, expected):
    fake_input(inputs)

    actual = student.ask_for_feedback(50)
    assert expected == actual
