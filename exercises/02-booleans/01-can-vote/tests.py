import pytest
from student import *


@pytest.mark.parametrize("argument", range(18, 100))
def test_can_vote(argument):
    assert can_vote(argument)


@pytest.mark.parametrize("argument", range(0, 18))
def test_cannot_vote(argument):
    assert not can_vote(argument)
