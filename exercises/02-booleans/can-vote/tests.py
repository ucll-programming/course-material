import pytest
import student


@pytest.mark.parametrize("argument", range(18, 100))
def test_can_vote(argument):
    assert student.can_vote(argument)


@pytest.mark.parametrize("argument", range(0, 18))
def test_cannot_vote(argument):
    assert not student.can_vote(argument)
