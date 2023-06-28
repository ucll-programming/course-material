import pytest
import student


@pytest.mark.parametrize("queue_size, target_size, expected", [
    (8, 5, 1),
    (8, 4, 1),
    (8, 3, 2),
    (8, 2, 2),
    (100, 99, 1),
    (100, 50, 1),
    (100, 49, 2),
    (100, 26, 2),
    (100, 25, 2),
    (100, 24, 3),
])
def test_thanos(queue_size, target_size, expected):
    actual = student.thanos(queue_size=queue_size, target_size=target_size)
    assert expected == actual, f'thanos({queue_size}, {target_size}) should return {expected} but instead returned {actual}'
