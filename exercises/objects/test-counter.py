import pytest
import student



@pytest.fixture
def counter():
    return student.Counter()


def test_initialization(counter):
    assert counter.count == 0


def test_increment(counter):
    counter.increment()
    assert counter.count == 1


def test_increment_twice(counter):
    counter.increment()
    counter.increment()
    assert counter.count == 2


def test_reset(counter):
    # Arrange
    counter.increment()

    # Act
    counter.reset()

    # Assert
    assert counter.count == 0
