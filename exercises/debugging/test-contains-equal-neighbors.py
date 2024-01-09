import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs", [
    [1, 1],
    [1, 1, 2, 3],
    [4, 2, 3, 5, 5, 4, 9],
    [4, 2, 3, 5, 4, 9, 9],
])
def test_contains_equal_neighbors(xs):
    assert student.contains_equal_neighbors(xs)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs", [
    [],
    [1],
    [1, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])
def test_not_contains_equal_neighbors(xs):
    assert not student.contains_equal_neighbors(xs)
