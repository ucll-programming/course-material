import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns", [
    *(
        tuple(range(a, b))
        for a in range(0, 10)
        for b in range(a, 10)
    ),
    ('a', 'b', 'c', 'd', 'e'),
])
def test_split_in_two(ns):
    actual_left, actual_right = student.split_in_two(ns)

    assert (*actual_left, *actual_right) == ns
    assert abs(len(actual_left) - len(actual_left)) <= 1
